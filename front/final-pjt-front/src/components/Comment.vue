<template>
	<!-- 수정 -->
	<div v-if="isEdit" class="commentPlace">
		<img class="commentProfile" src="https://assets.request-support.com/images/no_profile.gif?ver=1" alt="profile_image">

		<div>
			<div class="commentMain">
				<div class="commentTitle">{{ store.user.username }}: </div>
				<form @submit.prevent="updateComment" class="updateForm">
					<textarea class="commentContent" v-model.trim="content" name="content" id="content"></textarea>
					<button v-if="isLoginUserComment" class="commentBtn">수정</button>
					<button class="commentBtn" @click="isEdit=!isEdit">취소</button>
				</form>
			</div>
		</div>
	</div>

	<!-- 조회 -->
	<div v-else class="commentPlace">
		<img class="commentProfile" src="https://assets.request-support.com/images/no_profile.gif?ver=1" alt="profile_image">
		
		<div>
			<div class="commentMain">
				<div class="commentTitle">{{ store.user }}: </div>
				<div class="commentContent">{{ comment.content }}</div>
			</div>
			<button v-if="isLoginUserComment" class="commentBtn" @click="isUpdate">수정</button>
			<button v-if="isLoginUserComment" class="commentBtn" @click="deleteComment">삭제</button>
		</div>
	</div>
</template>
<script setup>
import { onMounted, ref, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useCounterStore } from '../stores/account'; 
import { useMovieStore } from '../stores/movie';

const props = defineProps({
	comment: Object,
})


const store = useCounterStore()
const router = useRouter()
const movieStore = useMovieStore()
const isEdit = ref(false)
const content = ref(props.comment.content)
const username = ref('')

onMounted(store.findUser(props.comment.user))

console.log(store.user)


const isLoginUserComment = store.loginUser.id === props.comment.user

const isUpdate = function () {
	isEdit.value = !isEdit.value
}

watch(movieStore.comments, (newComments) => {
	movieStore.comments = newComments
})

const deleteComment = function () {
	movieStore.deleteComment(props.comment?.id)
}

const updateComment = function () {
	if (!content.value) {
    alert('내용을 입력해주세요!')
    return
  }
  const payload = {
    commentId: props.comment.id,
    content: content.value,
  }
  movieStore.updateComment(payload)
  isEdit.value = !isEdit.value
}

</script>
  
<style scoped>
.commentPlace {
	margin-bottom: 20px;
	color: white;
	display: flex;
	align-items: start; /* 상단 정렬을 위해 추가 */
}

.commentPlace div {
	display: flex;
	width: 100%;
	justify-content: space-between;
	align-items: center;
}

.commentMain {
	flex-direction: column;
}

.commentTitle {
	display: block;
	font-size: 13px;
	font-weight: 400;
}

.commentContent {
	display: block;
	font-size: 14px;
	font-weight: 400;
	margin-bottom: 10px; /* 내용과 버튼 사이의 간격 추가 */
}

.commentBtn {
	height: 30px;
	width: 60px;
	background-image: linear-gradient(-90deg, #ff6b6b 0%, #c0392b 100%);
	color: white;
	border: none;
	border-radius: 5px;
	cursor: pointer;
	transition: background-color 0.3s;
}

.commentBtn:hover {
	background-image: linear-gradient(-90deg, #ff8c8c 0%, #e74c3c 100%);
}


/* 수정 스타일 */
.updateForm {
	width: 100%;
}

.updateForm textarea {
  background: none;
  border: 1px solid white;
  width: 100%;
  height: auto;
  min-height: 50px;
  overflow: auto;
  color: white;
  box-sizing: border-box;
  border-radius: 5px;
}

textarea::placeholder {
  white-space: pre-line;
  opacity: 0.5;
  font-size: 15px;
}
</style>

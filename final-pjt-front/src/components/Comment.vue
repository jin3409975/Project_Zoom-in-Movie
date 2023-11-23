<template>
	<!-- 수정 -->
	<div v-if="isEdit" class="commentPlace">
		<img class="commentProfile" src="https://assets.request-support.com/images/no_profile.gif?ver=1" alt="profile_image">

		<div>
			<div class="commentMain">
				<div class="commentTitle">{{ writer }}: </div>
				<form @submit.prevent="updateComment" class="updateForm">
					<input class="commentContent" v-model.trim="content" name="content" id="content">
					<button v-if="isLoginUserComment" class="commentBtn leftBtn">수정</button>
					<button class="commentBtn rightBtn" @click="isEdit=!isEdit">취소</button>
				</form>
			</div>
		</div>
	</div>

	<!-- 조회 -->
	<div v-else class="commentPlace">
		<img class="commentProfile" src="https://assets.request-support.com/images/no_profile.gif?ver=1" alt="profile_image">
		
		<div>
			<div class="commentMain">
				<div class="commentTitle">{{ writer }}: </div>
				<div class="commentContent">{{ comment.content }}</div>
			</div>
			<div class="comment-btn-div">
				<button v-if="isLoginUserComment" class="commentBtn leftBtn" @click="isUpdate">수정</button>
				<button v-if="isLoginUserComment" class="commentBtn rightBtn" @click="deleteComment">삭제</button>
			</div>
		</div>
	</div>
</template>
<script setup>
import { ref, watch, onMounted } from 'vue';
import { useCounterStore } from '../stores/account'; 
import { useMovieStore } from '../stores/movie';

const props = defineProps({
	comment: Object,
})


const store = useCounterStore()
const movieStore = useMovieStore()
const isEdit = ref(false)
const content = ref(props.comment.content)
const writer = ref(props.comment.user.username)
const isLoginUserComment = ref(store.loginUser.id === props.comment.user.id)

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
	align-items: start;
}

.commentPlace > div {
	width: 100%;
	display: flex;
	justify-content: space-between;
	align-items: center;
}

.commentMain {
	width: 100%;
}

.comment-btn-div {
	width: 110px;
	display: flex;
	justify-content: end;
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
	margin-bottom: 10px;
}

.commentBtn {
	height: 30px;
	width: 55px;
	color: white;
	border: none;
	cursor: pointer;
	transition: background-color 0.3s;
}

.leftBtn {
	border-radius: 5px 0 0 5px;
	background-image: linear-gradient(-90deg, #ff6b6b 0%, #c0392b 100%);
}

.rightBtn {
	border-radius: 0 5px 5px 0;
	background-image: linear-gradient(90deg, #ff6b6b 0%, #c0392b 100%);
}

.leftBtn:hover {
	background-image: linear-gradient(-90deg, #ff8c8c 0%, #e74c3c 100%);
}

.rightBtn:hover {
	background-image: linear-gradient(90deg, #ff8c8c 0%, #e74c3c 100%);
}


/* 수정 스타일 */
.updateForm {
	width: 100%;
}

.updateForm input {
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

input::placeholder {
  white-space: pre-line;
  opacity: 0.5;
  font-size: 15px;
}
</style>

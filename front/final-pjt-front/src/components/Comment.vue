<template>
	<div class="commentPlace">
		<img class="commentProfile" src="https://assets.request-support.com/images/no_profile.gif?ver=1" alt="profile_image">
		
		<div>
			<div class="commentMain">
				<div class="commentTitle">{{ store.user.username }}: </div>
				<div class="commentContent">{{ comment.content }}</div>
			</div>
			<button class="commentDelete" @click="deleteComment">삭제</button>
		</div>
	</div>
</template>
  
<script setup>
import { onMounted } from 'vue';
import { useCounterStore } from '../stores/account'; 

const store = useCounterStore()
const props = defineProps({
comment: Object
})

onMounted(() => {
	store.findUser(props.comment.user)
})

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

.commentDelete {
	
	height: 30px;
	width: 60px;
	border: none; /* 테두리 제거 */
	border-radius: 15px; /* 모서리 둥글게 */
	background-color: #f05454; /* 배경색 변경 */
	color: white; /* 텍스트 색상 변경 */
	box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* 그림자 효과 추가 */
	cursor: pointer; /* 마우스 오버 시 커서 변경 */
	font-size: 12px; /* 글꼴 크기 조정 */
	transition: background-color 0.3s; /* 부드러운 색상 변화 효과 */
}

.commentDelete:hover {
	background-color: #ff7675; /* 마우스 오버 시 배경색 변경 */
}
</style>

<template>
	<div class="commentPlace">
		<img class="commentProfile" src="https://assets.request-support.com/images/no_profile.gif?ver=1" alt="profile_image">
		<div>
			<span class="comment-id">{{ store.user.username }}: </span>
			<span class="comment-content">{{ comment.content }}</span>
			<button @click="deleteComment">🗑︎</button>
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
	console.log(props.comment.user)
	store.findUser(props.comment.user)
})

</script>
  
<style scoped>
  .commentPlace {
		margin-bottom: 20px;
		color: white;
		display: flex;
  }

	.commentPlace div {
		display: flex;
		align-items: center;
	}
</style>
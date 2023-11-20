<template>
	<div class="commentPlace">
		<img class="commentProfile" src="https://assets.request-support.com/images/no_profile.gif?ver=1" alt="profile_image">
		<div>
			<span class="comment-id">작성자: </span>
			<span class="comment-content">댓글 내용</span>
			<button @click="deleteComment">🗑︎</button>
		</div>
	</div>
</template>
  
  <script setup>
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
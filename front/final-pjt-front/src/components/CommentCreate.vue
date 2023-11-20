<template>
  <div class="commentCreateDiv">
    <img class="commentProfile" src="https://assets.request-support.com/images/no_profile.gif?ver=1" alt="profile_image">
    <form @submit.prevent="createComment">
      <textarea name="content" id="content" placeholder="댓글을 입력해주세요. &#13;&#10;스포성 댓글은 규정 위반이며 무통보 삭제 처리 될 수 있습니다."></textarea>
      <hr>
      <button>댓글 작성</button>
    </form>
  </div>
</template>

<script setup>

</script>

<style scoped>
.commentCreateDiv {
  display: flex;
}

form {
  width: 100%;
}

form textarea {
  background: none;
  border: none;
  width: 100%;
  height: auto;
  min-height: 50px;
  overflow: auto;
  color: white;
}

textarea::placeholder {
  white-space: pre-line;
  opacity: 0.5;
  font-size: 15px;
}

form button {
  display: block;
  margin: 0 0 0 auto;
  padding: 10px 20px;
  background-color: rgb(248, 47, 98, 0.3);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

form button:hover {
  background-color: rgb(248, 47, 98, 0.6);
  transform: scale(1.05);
}

hr {
  margin: 1% 0 2%;
  border-color: white;
  width: 100%;
}
</style>
<template>
  <div class="commentCreateDiv">
    <img class="commentProfile" src="https://assets.request-support.com/images/no_profile.gif?ver=1" alt="profile_image">
    <form @submit.prevent="createComment">
      <input v-model.trim="content" name="content" id="content" placeholder="댓글을 입력해주세요. &#13;&#10;스포성 댓글은 규정 위반이며 무통보 삭제 처리 될 수 있습니다.">
      <hr>
      <button>댓글 작성</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '../stores/movie';

const movieStore = useMovieStore()
const props = defineProps({
  movieId: Number,
})
const content = ref(null)

const createComment = function () {
  if (!content.value) {
    alert('내용을 입력해주세요!')
    return
  }

  const payload = {
    movieId: props.movieId,
    content: content.value,
  }
  movieStore.createComment(payload)
  content.value=''
}

</script>

<style scoped>
.commentCreateDiv {
  display: flex;
}

form {
  width: 100%;
}

form input {
  background: none;
  border: none;
  width: 100%;
  height: auto;
  min-height: 50px;
  overflow: auto;
  color: white;
}

input::placeholder {
  white-space: pre-line;
  opacity: 0.5;
  font-size: 15px;
}

form button {
  display: block;
  margin: 0 0 0 auto;
  padding: 10px 20px;
  background-image: linear-gradient(-90deg, #ff6b6b 0%, #c0392b 100%);
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

form button:hover {
  background-image: linear-gradient(-90deg, #ff8c8c 0%, #e74c3c 100%);
  transform: scale(1.05);
}

hr {
  margin: 1% 0 2%;
  border-color: white;
  width: 100%;
}
</style>
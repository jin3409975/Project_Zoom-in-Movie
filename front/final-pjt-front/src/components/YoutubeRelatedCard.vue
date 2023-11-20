<template>
    <div class="movie-card">
      <div class="movie-image">
        <img :src="movieImageUrl" alt="영화 이미지" />
      </div>
      <div class="movie-info">
        <h2 class="movie-title">{{ movieTitle }}</h2>
        <p class="movie-description">{{ movieDescription }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const movieImageUrl = ref('https://occ-0-1360-993.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABR5FB85jaUHWFtM7ZfwmJQI6Ai1d6j6n2KRDm9CmL5bJ8Pbe5Mabq4LAb5F2mCD65iBatdWpTm0kAQE5cuSl5f8wyH6IepnWY4I.webp?r=94a'); // 영화 이미지 URL
  const movieTitle = ref('독전2');
  const movieDescription = ref('한국의 로맨스 웹툰. 작가는 나노리스트를 연재한 민송아. 이번에도 그림체와 인물 표현이 전작과 비슷하다. 그리고 부제는 ~두근두근 누나리스트~');
  </script>
  
  <style scoped>
  .movie-card {
    display: flex;
    background-color: #141414;
    color: #fff;
    margin-bottom: 20px;
    display: flex;
    flex-direction: column;
    width: 300px;
  }
  
  .movie-image img {
    width: 100%;
    height: auto;
	border-radius: 8px 8px 0 0;
    margin-right: 20px;
  }
  
  .movie-info {
    height: 200px;
    padding-top: 7%;
    padding-left: 5%;
    display: flex;
    flex-direction: column;
	border-radius: 0 0 8px 8px;
    background-color: #2F2F2F;
    overflow: hidden;
  }
  
  .movie-title {
    margin: 0;
    font-size: 24px;
  }
  
  .movie-description {
    font-size: 16px;
  }
  </style>
  
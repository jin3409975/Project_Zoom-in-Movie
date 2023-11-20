<template>
  <div class="mainBackColor backSize">
    <!-- 케러셀 -->
    <div class="carouselSize">
      <div id="carouselExampleIndicators" class="carousel slide marginMid" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner marginMid">
          <div class="carousel-item active" data-bs-interval="4500">
            <img src="https://occ-0-988-993.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABRB8wiQJXy6Ecwac6ye3koG50Hx36a5ljm_e6o4BXnl_becinwzUH9HZvVWYRHpeRAdPLZcYkYlVI0KxHi7rzQoJTpoV2H_9BHts.webp?r=6df" class="d-block w-100 rounded" alt="#">
          </div>
          <div class="carousel-item" data-bs-interval="4500">
            <img src="https://occ-0-988-993.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABWVW0OpxSD0EVQlMznHowIIKBSSgL2BHrse2laXLGrb4zeLBFP4UmOY3I874f3gPROtcUp8BIXFxCrDgJbZAwxFQhZAW2hBVeds.webp?r=c4c" class="d-block w-100 rounded" alt="#">
          </div>
          <div class="carousel-item" data-bs-interval="4500">
            <img src="https://image.tmdb.org/t/p/w500/t5zCBSB5xMDKcDqe91qahCOUYVV.jpg" class="d-block w-100 rounded" alt="#">
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </div>

    <!-- <h1 class="listTitle">일단넘겨 인기 콘텐츠</h1>
    <main class="movieList">
        <MovieCard class="movieCard"/>
    </main> -->

    <h1 class="listTitle">일단넘겨 인기 콘텐츠</h1>
    <main class="movieList">
      <MovieCard 
      v-for="movie in movies" :key="movie.id" :movie="movie" 
      class="movieCard"/>
    </main>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import MovieCard from '../components/MovieCard.vue'

const store = useCounterStore()

onMounted(() => {
  store.getMovies()
})

</script>

<style scoped>
/* 캐러셀 기본 설정 */
.carouselSize {
	height: 50vh;
	max-width: 900px;
	width: auto;
  top: 1px;
  margin: 0 auto;
  overflow: hidden;
}

.carousel-inner, .carousel {
  overflow: hidden;
	width: 100%;
}

/* 캐러셀 아이템 설정 */
.carousel-item {
	height: 50vh;
	width: 100%;
  border-radius: 10px;
  overflow: hidden;
  transition: transform 0.5s ease;
}

/* 캐러셀 이미지 설정 */
.carousel-item img {
	height: 100%;
	width: auto;
  object-fit: cover;
  border-radius: 10px;
}

.carousel-item:hover {
    transform: rotate(10deg) scale(1.1) translateX(5px);
    transition: transform 0.3s ease;
    /* transform: scale(1.05); */
}
</style>
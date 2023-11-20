<template>
  <div class="mainBackColor backSize">
    <!-- 케러셀 -->
    <div class="carouselSize">
      <div id="carouselExampleIndicators" class="carousel slide marginMid" data-bs-ride="carousel">
        <!-- 아래 버튼 -->
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button v-for="i in 4" type="button" data-bs-target="#carouselExampleIndicators" :data-bs-slide-to="i" :aria-label="`Slide ${i + 1}`"></button>
        </div>
        <!-- 케루젤 이미지 -->
        <div class="carousel-inner marginMid">
          <div class="carousel-item active" data-bs-interval="4500">
            <img @click="goDetail(store.movies[0].movie_id)" :src="`https://image.tmdb.org/t/p/original${store.movies[0]?.backdrop_path}`" class="d-block w-100 rounded" alt="#">
          </div>
          <div v-for="i in 4" class="carousel-item" data-bs-interval="4500">
            <img @click="goDetail(store.movies[i].movie_id)" :src="`https://image.tmdb.org/t/p/original${store.movies[i]?.backdrop_path}`" class="d-block w-100 rounded" alt="#">
          </div>
        </div>
        <!-- 좌우 버튼 -->
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

    <!-- 인기순 -->
    <h1 class="listTitle">일단넘겨 인기 콘텐츠</h1>
    <main class="movieList">
      <MovieCard 
      v-for="movie in store.movies" :key="movie.id" :movie="movie" 
      class="movieCard"/>
    </main>

  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useRouter } from 'vue-router';
import { useMovieStore } from '@/stores/movie.js'
import MovieCard from '../components/MovieCard.vue'
import YoutubeRelatedCard from '../components/YoutubeRelatedCard.vue';

const store = useMovieStore()
const router = useRouter()

onMounted(() => {
  store.getPopularMovies()
})

const goDetail = function (movieId) {
    router.push({ name: 'MovieDetailView', params: { movieId: movieId} })
}
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

.carousel-item img:hover {
  cursor: pointer;
}

.carousel-item:hover {
    transform: rotate(10deg) scale(1.1) translateX(5px);
    transition: transform 0.3s ease;
    /* transform: scale(1.05); */
}
</style>
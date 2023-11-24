<template>
  <div class="mainBackColor backSize side-padding-zero-important main-place">
    <h1 id="backTitle" @click="goDetail(backMovie.movie_id)">{{ backTitle }}</h1>
    <div class="typing-place">
      <img @click="goDetail(backMovie.movie_id)" :src="backUrl" alt="#">
      <AboutView class="typing" :movieTitle="backTitle" :idx="randomIdx"/>
      <Scroll/>
    </div>

    <!-- 인기순 -->
    <div class="main-main">
      <h1 class="listTitle">ZnMovie 인기 콘텐츠</h1>
      <main class="movieList">
        <MovieCard
         v-for="movie in movieStore.popularMovies"
         :key="movie.id"
         :movie="movie"
         class="movieCard"
        />
      </main>
      <Footer/>
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'
import { useRouter } from 'vue-router';
import { random } from 'lodash'
import { useMovieStore } from '@/stores/movie.js'
import MovieCard from '../components/MovieCard.vue'
import AboutView from '../components/AboutView.vue'
import Footer from '../components/Footer.vue';
import Scroll from '@/components/Scroll.vue'
const defaultMovie = { 
  actors: [],
  adult: false,
  backdrop_path: "/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",
  genres: (2) [18, 36],
  id: 1,
  movie_id: "872585",
  original_title: "Oppenheimer",
  overview: "세상을 구하기 위해 세상을 파괴할 지도 모르는 선택을 해야 하는 천재 과학자의 핵개발 프로젝트.",
  popularity: 2718.643,
  poster_path: "/4ZLnVUfiCe3wX8Ut9eyujndpyvA.jpg",
  rating: 8.189,
  release_date: "2023-07-19",
  runtime: 181,
  title: "오펜하이머" }

const router = useRouter()
const movieStore = useMovieStore()

const randomIdx = ref(random(0, 5))
const backMovie = movieStore.popularMovies[randomIdx.value] || defaultMovie
const backUrl = `https://image.tmdb.org/t/p/original${backMovie.backdrop_path}`
const backTitle = backMovie.title

const goDetail = function (movieId) {
    router.push({ name: 'MovieDetailView', params: { movieId: movieId} })
}
</script>

<style scoped>
#backTitle {
  position: absolute;
  color: white;
  z-index: 99999999999999999;
  left: 50%;
  top: -3.5%;
  transform: translate(-50%, -50%);
  font-family: fantasy;
  font-size: 40px;
  font-weight: 600;
  cursor: pointer;
}

@media (max-width: 1400px) {
  #backTitle {
    display: none;
 }
}

.main-place{
  position: relative;
  height: 100%;
}

.typing-place {
  width: 100%;
  position: absolute;
  z-index: 0;
}
.typing-place img {
  position: relative;
  width: 100%;
  max-height: 100%;
  overflow: hidden;
  background-position: center;
  z-index: 0;
  cursor: pointer;
}

.typing-place::before {
  content: '';
  background-image: linear-gradient(to top, #141414, transparent);
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100%;
  width: 100%;
  z-index: 1;
  pointer-events: none;
}

.typing {
  position: absolute;
  top: 70%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
  color: white;
  text-align: center;
  pointer-events: none;
  width: 100%;
}


.main-main {
  padding: 0 3.5%;
  z-index: 1;
  position: absolute;
  margin-top: 45%;
}

.main-main h1 {
  margin-left: 1.5%;
}
</style>
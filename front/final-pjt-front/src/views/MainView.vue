<template>
  <div class="mainBackColor backSize side-padding-zero-important main-place">
    <div class="typing-place">
      <img @click="goDetail(backMovie.movie_id)" :src="backUrl" alt="#">
      <AboutView class="typing" :movieTitle="backTitle" :idx="randomIdx"/>
    </div>

    <!-- 인기순 -->
    <div class="main-main">
      <h1 class="listTitle">일단넘겨 인기 콘텐츠</h1>
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
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router';
import { random } from 'lodash'
import { useMovieStore } from '@/stores/movie.js'
import MovieCard from '../components/MovieCard.vue'
import AboutView from '../components/AboutView.vue'
import Footer from '../components/Footer.vue';

const router = useRouter()
const movieStore = useMovieStore()

const randomIdx = ref(random(0, 5))
const backMovie = ref(movieStore.popularMovies[randomIdx.value])
const backUrl = ref(backMovie.value.backdrop_path)
const backTitle = ref(backMovie.value.title)

onMounted(() => {
  movieStore.getPopularMovies()
})

const goDetail = function (movieId) {
    router.push({ name: 'MovieDetailView', params: { movieId: movieId} })
}

if (backUrl) {
    backUrl.value = `https://image.tmdb.org/t/p/original${backUrl.value}`
} else {
    backUrl.value = 'https://an2-img.amz.wtchn.net/image/v2/v_rtGmsGmmSGuScg0hC76g.webp?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1KbklsMHNJbkFpT2lJdmRqSXZjM1J2Y21VdmFXMWhaMlV2TVRZNE5Ea3hOVGN4T1RJM05UQTVOVGs0TXlKOS5mRjlhcmYwZWNJd2cyNUl4YnBfZkZyV0E5UmpkMnhLdmVEUnhUUU1jUXN3'
}
</script>

<style scoped>
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
  top: 65%; /* 상위 요소의 중앙에 위치하도록 top 값을 50%로 설정 */
  left: 50%; /* 상위 요소의 중앙에 위치하도록 left 값을 50%로 설정 */
  transform: translate(-50%, -50%); /* 자신의 크기의 절반만큼 오프셋을 줘서 완벽하게 중앙에 배치 */
  z-index: 2; /* 이미지 위에 오도록 z-index 설정 */
  color: white; /* 텍스트 색상을 흰색으로 설정 */
  text-align: center; /* 텍스트를 가운데 정렬 */
  pointer-events: none;
  width: 100%; /* 가로 전체를 사용하도록 설정 */
}


.main-main {
  padding: 0 3.5%;
  z-index: 1;
  position: absolute;
  margin-top: 40%;
}

.main-main h1 {
  margin-left: 1.5%;
}
</style>
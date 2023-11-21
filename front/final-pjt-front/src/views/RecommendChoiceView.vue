<template>
    <div class="backSize mainBackColor midDisplay">
        <div class="choicePlace">
            <div class="choiceTitle">
                <h2>좋아하는 콘텐츠를 3개 선택하세요.</h2>
                <p>취향에 꼭 맞는 시리즈와 영화를 찾아드리는 데 도움이 됩니다. 마음에 드는 콘텐츠를 선택하세요.</p>
            </div>
            <div class="movieList">
                <MoviePoster 
                @click="checkMovie(movie.id)" v-for="movie in store.movies" :key="movie.id" :movie="movie" 
                 />
            </div>
            <button v-if="selectedMovies.length === 3" @click="completeSelection">컨텐츠 선택 완료></button>
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useMovieStore } from '../stores/movie';
import MoviePoster from '../components/MoviePoster.vue'
import { ref } from 'vue'


const store = useMovieStore()

onMounted(() => {
  store.getPopularMovies()
})

const selectedMovies = ref([])

// 클릭하면서 함수 안에서 포스터를 체크해서 css를 적용해주고 
// css는 이거 >> .movie-card:hover .movie-overlay {opacity: 1;}
// 해당 영화를 빈 배열에 담고, 3개가 되면 오른쪽 아래에 컨텐츠 선택 완료 버튼이 나타나게.
const checkMovie = function (movieId) {
    if (!selectedMovies.value.includes(movieId)) {
        selectedMovies.value.push(movieId);
    }
}

const completeSelection = function () {
    // 여기에 선택 완료 후 실행할 로직 추가
    console.log("선택된 영화:", selectedMovies.value)
}
</script>

<style scoped>
.choicePlace {
    display: flex;
}

.choiceTitle {
    display: inline;
    color: white;
    font-family: Helvetica, sans-serif;
    margin: 0 0 .4em;
    width: 200%;
    padding: 50px 3px 0 0;
}

.choiceTitle h1 {
    font-weight: 500;
    line-height: 1.2;
}
</style>
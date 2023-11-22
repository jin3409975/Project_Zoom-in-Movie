<template>
    <div class="mainBackColor backSize">
        <h1 class="listTitle">{{ store.loginUser.username }}님에게 추천하는 영화</h1>
        <main class="movieList" v-for="movies in movieStore.recommendMovies">
            <MovieCard
                v-for="movie in movies" 
                :key="movie.id" :movie="movie" 
                class="movieCard"/>
        </main>
    </div>
</template>

<script setup>
import { watch } from 'vue';
import MovieCard from '../components/MovieCard.vue';
import { useCounterStore } from '../stores/account';
import { useMovieStore } from '../stores/movie';

const store = useCounterStore()
const movieStore = useMovieStore()

store.checkLoginUser()
movieStore.movieRecommend()

watch(() => movieStore.recommendMovies, (newRecommendMovies) => {
    movieStore.recommendMovies = newRecommendMovies
}, { immediate: true })




</script>

<style scoped>

</style>
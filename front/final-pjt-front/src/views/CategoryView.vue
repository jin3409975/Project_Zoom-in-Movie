<template>
    <div class="mainBackColor backSize">
        <h1 class="listTitle">"{{ genre }}" 관련된 영화를 모아봤어요</h1>
        <main class="movieList">
            <MovieCard 
                v-for="movie in store.movies" :key="movie.id" :movie="movie" 
                class="movieCard"/>
        </main>
    </div>
</template>

<script setup>
import { onMounted, watch, ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useMovieStore } from '../stores/movie';
import MovieCard from '../components/MovieCard.vue';

const route = useRoute()
const store = useMovieStore()
const genre = ref(route.params.genre)

watch(() => route.params.genre, (newGenre) => {
  store.getGenreMovie(newGenre);
  genre.value = newGenre
}, { immediate: true });

</script>

<style scoped>

</style>
<template>
    <div class="movie-card">
        <img @click="goDetail" class="movie-image" :src="img_url" :alt="movie.title">
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()
const props = defineProps({
    movie: Object,
})

const poster_path = props.movie.poster_path
const img_url = `https://image.tmdb.org/t/p/original${poster_path}`

const goDetail = function () {
    router.push({ name: 'MovieDetailView', params: { movieId: props.movie.movie_id} })
}

</script>

<style scoped>
.movie-card {
    width: 22%;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease-in-out;
    margin: 0 1.5% 5%;
}

.movie-card:hover {
    transform: scale(1.05);
    cursor: pointer;
}

.movie-image {
    width: 100%;
    height: 100%;
    display: block;
}

</style>

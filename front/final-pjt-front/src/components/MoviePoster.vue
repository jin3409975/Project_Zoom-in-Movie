<template>
    <div class="movie-card">
        <img @click="goDetail" class="movie-image" :src="img_url" :alt="movie.title">
        <div class="movie-overlay">
            <i class="fa fa-thumbs-up like-icon"></i>
        </div>
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
  width: 200px;
  position: relative;
  cursor: pointer;
}

.movie-card:hover {
  transform: scale(1.04);
  transition: transform 0.3s ease;
}

.movie-image {
  width: 200px;
  display: block;
  border-radius: 4px;
  transition: transform 0.3s ease;
}

.movie-overlay {
  width: 200px;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  color: white;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: opacity 0.3s ease;
  font-size: 15px;
}

.movie-card:hover .movie-overlay {
  opacity: 1;
}

.like-icon {
  font-size: 3em;
}
</style>
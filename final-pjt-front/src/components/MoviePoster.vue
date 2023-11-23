<template>
    <div class="movie-card" @mouseenter="showOverlay" @mouseleave="hideOverlay">
        <img @click="goDetail" class="movie-image" :src="img_url" :alt="movie.title">
        <div class="movie-overlay" v-show="isOverlayVisible">
            <i class="fa fa-thumbs-up like-icon" :class="{ 'liked': isLiked }" @click.stop="toggleLike"></i>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const props = defineProps({
    movie: Object,
})

const isOverlayVisible = ref(false)
const isLiked = ref(false)

const poster_path = props.movie.poster_path
const img_url = `https://image.tmdb.org/t/p/original${poster_path}`

const goDetail = function () {
    router.push({ name: 'MovieDetailView', params: { movieId: props.movie.movie_id} })
}

const toggleLike = async () => {
  isLiked.value = !isLiked.value
  isOverlayVisible.value = true
}

const showOverlay = () => {
  // 마우스가 올라왔을 때 오버레이를 보여줌
  isOverlayVisible.value = true;
}

const hideOverlay = () => {
  isOverlayVisible.value = true
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
  transition: color 0.3s ease;
}

.like-icon.liked {
  color: #007bff   /* 좋아요를 클릭했을 때의 색상 */
}
</style>
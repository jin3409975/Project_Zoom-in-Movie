<template>
    <div class="btnPlace">
        <button @click="likeBtn">
            <i v-if="isLiked" class="fa-solid fa-heart liked"></i>
            <i v-else class="far fa-heart"></i>
        </button>
    </div>
</template>

<script setup>
import { onMounted, watch, ref } from 'vue'
import { useMovieStore } from '@/stores/movie.js'

const movieStore = useMovieStore()
const isLiked = ref(false)

const props = defineProps({
    thisId: Number,
})

const likeBtn = () => {
    movieStore.updateLikeMovie(props.thisId)
    isLiked.value = movieStore.isLiked
}

watch(() => movieStore.isLiked, (newIsLiked) => {
    movieStore.checkLikeMovie(props.thisId)
    isLiked.value = newIsLiked
}, { immediate: true })
</script>

<style scoped>
button {
    border: none;
    background-color: transparent;
    cursor: pointer;
    outline: none;
    transition: transform 0.2s ease;
}

button:hover {
    transform: scale(1.1);
}

.btnPlace {
    margin-left: 5px;
    display: inline-block;
}

.fa-heart {
    color: red;
    opacity: 0.7;
    font-size: large;
    transition: color 0.2s ease;
}

.fa-heart.liked {
    opacity: 1;
    color: red;
    animation: pulse 1s infinite;
}

@keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.2);
    }
    100% {
        transform: scale(1);
    }
}
</style>

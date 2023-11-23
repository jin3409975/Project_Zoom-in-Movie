<template>
    <div class="videoDiv marginMid">
        <iframe width="560" height="315" :src="videoUrl" frameborder="0" allowfullscreen></iframe>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'

const props = defineProps({
    movieTitle: String,
})

const apiKey = import.meta.env.VITE_YOUTUBE_KEY
const videoId =  ref(null)
const videoUrl = ref(null)

// movieTitle의 변화가 있을 때마다 데이터를 새로 로드합니다.
watch(() => props.movieTitle, async (newMovieTitle) => {
  await loadMovieData(newMovieTitle)
}, { immediate: true })

// 영화 데이터와 예고편을 로드하는 함수
async function loadMovieData(movieTitle) {
  try {
    const response = await axios({
      method: 'get',
      url: `https://www.googleapis.com/youtube/v3/search`,
      params: {
        part: 'snippet',
        q: `${movieTitle} 공식 예고편`,
        type: 'video',
        key: apiKey
      }
    })
    videoId.value = response.data.items[0].id.videoId;
    videoUrl.value = `https://www.youtube.com/embed/${videoId.value}`
  } catch (err) {
    console.error("YouTube API 요청 중 오류 발생: ", err)
  }
}
</script>

<style scoped>
.videoDiv {
	display: flex;
	justify-content: center;
}

.videoDiv iframe {
	border-radius: 8px;
}
</style>
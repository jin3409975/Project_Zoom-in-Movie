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
            <button v-if="selectedMovies.length === 3" @click="completeSelection">콘텐츠 선택 완료</button>
        </div>
    </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useMovieStore } from '../stores/movie'
import MoviePoster from '../components/MoviePoster.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'


const store = useMovieStore()

onMounted(() => {
  store.getPopularMovies()
})

const router = useRouter()
const selectedMovies = ref([])
const completeSelection = async function () {
    console.log("선택된 영화:", selectedMovies.value)

    try {
        // 선택된 영화 목록을 Django로 전송
        const response = await axios.post('http://127.0.0.1:5173/<int:user_pk>/like/comment/', {
            like_movies: selectedMovies.value,
            // 다른 필요한 데이터가 있다면 여기에 추가
        })

        // Django에서 반환한 데이터를 콘솔에 출력
        console.log('Response from Django:', response.data);

        // 여기에서 필요한 UI 업데이트나 라우팅 등을 수행할 수 있습니다.

    } catch (error) {
        console.error('Error sending selected movies:', error);
    }

    // 선택이 완료되면 MainView로 이동
    router.push({ name: 'MainView' })
}


// 클릭하면서 함수 안에서 포스터를 체크해서 css를 적용해주고 
// css는 이거 >> .movie-card:hover .movie-overlay {opacity: 1;}
// 해당 영화를 빈 배열에 담고, 3개가 되면 오른쪽 아래에 컨텐츠 선택 완료 버튼이 나타나게.
const checkMovie = function (movieId) {
    if (!selectedMovies.value.includes(movieId)) {
        selectedMovies.value.push(movieId);
    }
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
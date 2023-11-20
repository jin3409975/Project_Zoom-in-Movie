<template>
    <div class="backSize mainBackColor midDisplay">
        <div class="choicePlace">
            <div class="choiceTitle">
                <h2>좋아하는 콘텐츠를 3개 선택하세요.</h2>
                <p>취향에 꼭 맞는 시리즈와 영화를 찾아드리는 데 도움이 됩니다. 마음에 드는 콘텐츠를 선택하세요.</p>
            </div>
            <div class="movieList">
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
                <MoviePoster/>
            </div>
        </div>
    </div>
</template>

<script setup>
import MoviePoster from '../components/MoviePoster.vue';
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
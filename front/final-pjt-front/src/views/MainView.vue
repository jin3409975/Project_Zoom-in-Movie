<template>
    <div class="mainBack backSize">
        <!-- 케루젤 -->
        <div id="carouselExampleIndicators" class="carousel slide carouselSize" data-bs-ride="carousel">
            <div class="carousel-indicators">
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
            </div>
            <div class="carousel-inner">
                <div class="carousel-item active" data-bs-interval="4500">
                <img src="https://occ-0-988-993.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABRB8wiQJXy6Ecwac6ye3koG50Hx36a5ljm_e6o4BXnl_becinwzUH9HZvVWYRHpeRAdPLZcYkYlVI0KxHi7rzQoJTpoV2H_9BHts.webp?r=6df" class="d-block w-100 rounded" alt="#">
                </div>
                <div class="carousel-item" data-bs-interval="4500">
                <img src="https://occ-0-988-993.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABWVW0OpxSD0EVQlMznHowIIKBSSgL2BHrse2laXLGrb4zeLBFP4UmOY3I874f3gPROtcUp8BIXFxCrDgJbZAwxFQhZAW2hBVeds.webp?r=c4c" class="d-block w-100 rounded" alt="#">
                </div>
                <div class="carousel-item" data-bs-interval="4500">
                <img src="https://image.tmdb.org/t/p/w500/t5zCBSB5xMDKcDqe91qahCOUYVV.jpg" class="d-block w-100 rounded" alt="#">
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>

        <h1 class="popularTitle">일단넘겨 인기 콘텐츠</h1>
        <main class="popularZone">
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            <MovieCard class="movieCard"/>
            
        </main>


    </div>
</template>

<script setup>
import MovieCard from '../components/MovieCard.vue';

</script>

<style scoped>
.carousel-item {
  transition: transform 0.5s ease;
}

.mainBack {
    background-color: #141414;
}

.popularZone {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: flex-start;
    gap: 20px;
    padding: 20px;
}
.popularTitle {
    color: white;
    font-family: 'Roboto', sans-serif;
    font-size: 2em;
    font-weight: bold;
    margin: 20px 20px 0 20px;
}


.carouselSize {
    width: 800px;
    margin: 0 auto;
    max-height: 400px;
    overflow: hidden;
}

.movieCard {
    background-color: #333;
    color: #fff;
    padding: 15px;
    margin: 15px;
    border-radius: 10px;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: transform 0.3s ease-in-out;
    width: 250px;
    margin: 0;
}

.movieCard:hover {
    transform: scale(1.1);
}

</style>
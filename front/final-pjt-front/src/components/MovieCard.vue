<template>
    <div class="movie-card">
        <img class="movie-image" src="https://occ-0-988-993.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABeHSyu8X6fwOdoSQmHsd0MQnE-ko8EEHz-jihj4Hm2lvwkcllFTsqlX_NJWlS3qpSrqDf7lpLzDLxfEP8S7KFwNBWfP4vasLy8qzKqgqLmqAteMUY_1S2SE5lp3cAOHLiyj06PnVkFFAvLuuEYDQ7xH3U5-4RoiSugzcJhdr4LG_3NGNN9y53VK7rk3pGOuKHJ1kFjcRT-ObTZp22D00sj0wb1V6wKPMGF7LraTY7ZWhQuYr1E9jMNuuPdUjXBmsE_bGb11cjQ6syEUT1ZNl8YWmwfibDUDeiswK4k4NArJgKSjIxO9SYcM.jpg?r=1c6" alt="영화 제목">
    </div>
</template>

<script setup>

</script>

<style scoped>
.movie-card {
    width: 200px;
    border-radius: 6px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease-in-out;
    margin-bottom: 11px;
    /* margin: 20px; */
}

.movie-card:hover {
    transform: scale(1.1);
}

.movie-image {
    width: 100%;
    display: block;
}

</style>

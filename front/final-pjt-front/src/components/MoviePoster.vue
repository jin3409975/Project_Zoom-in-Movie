<template>
    <div class="movie-card">
        <img src="https://occ-0-988-993.1.nflxso.net/dnm/api/v6/WNk1mr9x_Cd_2itp6pUM7-lXMJg/AAAABesSOhEyU1dvhMddc-kG6avKE43CcZXZRSuDfkJMSU0xHvkEf7sRW0kTCvYQXxkd0x0HWZ7BtgzJgU-J9oFPc5P7LIlvPlhb3A.jpg?r=dae" alt="Movie Title" class="movie-image">
        <div class="movie-overlay">
            <i class="fa fa-thumbs-up like-icon"></i>
        </div>
    </div>
</template>

<script setup>

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
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useMovieStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const movie = ref([])
  const movies = ref([])
  const genre = ref([])
  const genres = ref([])
  const comments = ref([])

  // DRF에 article 조회 요청을 보내는 action
  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`
    })
      .then((res) =>{
        // console.log(res.data)
        movies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getMovie = function (movieId) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movie/${movieId}/`
    })
      .then((res) =>{
        // console.log(res.data)
        movie.value = res.data
      })
      .then((res) => {
        genre.value = movie.value.genres.map((genreId) => {
          return genres.value.filter(g => g.genre_id === genreId)[0].genre_name
        })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getPopularMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/current_popularity/`
    })
      .then((res) =>{
        // console.log(res.data)
        movies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getGenres = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/genres/`
    })
      .then((res) =>{
        // console.log(res.data)
        genres.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getGenreMovie = function (genre) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/genres/${genre}/`
    })
      .then((res) =>{
        // console.log(res.data)
        movies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getComments = function (moviePk) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/${moviePk}/comment/`
    })
      .then((res) =>{
        // console.log(res.data)
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


  return { movie, movies, genre, genres, comments, getMovies, getMovie, getPopularMovies, getGenres, getGenreMovie, getComments }
}, { persist: true })

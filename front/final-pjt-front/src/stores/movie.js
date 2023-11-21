import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { useCounterStore } from './account'


export const useMovieStore = defineStore('counter', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const accountStore = useCounterStore()
  const movie = ref([])
  const movies = ref([])
  const genre = ref([])
  const genres = ref([])
  const comment = ref([])
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
  // movie 값이 변경되기 전에 리턴되어 예고편 영상이 이전 영화 예고편으로 나오는 코드
  // const getMovie = function (movieId) {
  //   axios({
  //     method: 'get',
  //     url: `${API_URL}/api/v1/movie/${movieId}/`
  //   })
  //     .then((res) =>{
  //       console.log(res.data)
  //       movie.value = res.data
  //       genre.value = movie.value.genres.map((genreId) => {
  //         return genres.value.filter(g => g.genre_id === genreId)[0].genre_name
  //       })
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //     })
  // }

  const getMovie = async function (movieId) {
    try {
      const res = await axios({
        method: 'get',
        url: `${API_URL}/api/v1/movie/${movieId}/`
      });
      // console.log(res.data);
      movie.value = res.data;
      genre.value = movie.value.genres.map((genreId) => {
        return genres.value.filter(g => g.genre_id === genreId)[0].genre_name;
      });
    } catch (err) {
      console.error(err);
    }
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
      url: `${API_URL}/api/v1/genre/${genre}/`
    })
      .then((res) =>{
        // console.log(res.data)
        movies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const getComments = function (movieId) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/${movieId}/comment/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
      .then((res) =>{
        // console.log(res.data)
        comments.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const createComment = function (payload) {
    const { movieId, content } = payload

    axios({
      method: 'post',
      url: `${API_URL}/api/v1/movies/${movieId}/comment/`,
      data: {
        content,
      },
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
      .then((res) =>{
        console.log(res.data)
        comments.value.unshift(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const deleteComment = function (commentId) {
    axios({
      method: 'delete',
      url: `${API_URL}/api/v1/comment/${commentId}/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
      .then((res) =>{
        const index = comments.value.findIndex(c => c.id === commentId);
        if (index !== -1) {
          comments.value.splice(index, 1);
        }
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const updateComment = function (payload) {
    const { commentId, content } = payload

    axios({
      method: 'put',
      url: `${API_URL}/api/v1/comment/${commentId}/`,
      data: {
        content,
      },
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
      .then((res) =>{
        // console.log(res.data)
        const index = comments.value.findIndex(c => c.id === commentId)
        if (index !== -1) {
          comments.value[index].content = content;
        }
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { movie, movies, genre, genres, comment, comments,
    getMovies, getMovie, getPopularMovies, getGenres, getGenreMovie,
    getComments, deleteComment, createComment, updateComment,
  }
}, { persist: true })

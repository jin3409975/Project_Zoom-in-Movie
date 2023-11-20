import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'



export const useCounterStore = defineStore('counter', () => {
  const movies = ref([])


  // DRF에 article 조회 요청을 보내는 action
  const getMovies = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/`
    })
      .then((res) =>{
        console.log(res)
        movies.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }


  return { movies, getMovies }
}, { persist: true })

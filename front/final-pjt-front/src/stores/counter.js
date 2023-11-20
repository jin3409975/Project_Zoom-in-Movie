import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'



// import Vue from 'vue'
// import Vuex from 'vuex'
// import axios from 'axios'
// import router from '@/router'
// import createPersistedState from "vuex-persistedstate";
// import swal from 'sweetalert2'
// import SERVER from '@/api/v1'


// Vue.use(Vuex)


// export default new Vuex.Store({
//   // 새로고침해도 state 정보 그대로
//   plugins: [createPersistedState()],

//   // state = 어플의 초기 상태 정의
//   state: {
//     // Oauth용 토큰
//     token: null,
//     // 계정 상황
//     userId: null,
//     isLogin: false,
//     username: null,
//     image: null,
//     // introduction: null,
//     // 댓글 작성 개수
//     comments_count: 0,
//     // 자주 방문하는 페이지 영화 프리로딩
//     movie: null,
//     movies: [],
//     moviesRecommend: [],
//   },

//   // getters = store 상태를 기반으로 파생된 상태를 계산하는 데 사용
//   getters: {
//     movie(state) {
//       return state.movie
//     },
//     movies(state) {
//       return state.movies
//     },
//     moviesRecommend(state) {
//       return state.moviesRecommend
//     },
//     token: function() {
//       const token = localStorage.getItem('jwt')
//       return {
//         Authorization: `JWT ${token}`,
//       };
//     },
//   },

//   // mutations = 상태 수정
//   mutations: {
//     // 계정 상태 변경
//     LOGIN(state, credentials) {
//       state.username = credentials.username
//       state.isLogin = true
//     },

//     LOGOUT(state) {
//       state.isLogin = false
//       state.userId = null
//       state.username = null
//       // state.introduction = null
//       state.image = null
//       state.token = null
//       state.comments_count = null
//       localStorage.removeItem("jwt");
//     },

//     // Oauth
//     SET_TOKEN(state, token) {
//       state.token = token
//     },

//     GET_USER_INFO(state, res) {
//       state.userId = res.id
//       // state.introduction = res.introduction
//       state.comments_count = res.comments_count
//       // if (res.image) {
//       //   //state.image = 'http://127.0.0.1:8000' + res.image  
//       //   // state.image = SERVER.ROUTES.image + res.image         
//       // } else {
//       //   state.image = null
//       // }
//     },

//     GET_MY_PROFILE(state, data){
//       state.image = data.image
//       state.introduction = data.introduction
//     },

//     GET_MOVIE(state, res) {
//       state.movie = res
//     },

//     GET_MOVIES(state, res) {
//       state.movies = res
//     },

//     GET_MOVIES_RECOMMEND(state, res) {
//       state.moviesRecommend = res
//     },
//   },

//   // actions = 비동기 호출을 수행하는 비즈니스 로직을 포함
//   actions: {
//     // 계정 상태 변경
//     login({commit}, credentials) {
//       axios({
//         method: 'POST',
//         //url: `${SERVER_URL}accounts/api-token-auth/`,
//         //route: SERVER.ROUTES.accounts.login,
//         //url: 'https://moviecurators.herokuapp.com/accounts/api-token-auth/',
//         url: SERVER.URL + SERVER.ROUTES.accounts.login,
//         data: credentials,
//       })
//       .then(res => {
//         localStorage.setItem('jwt', res.data.token)
//         commit('LOGIN', credentials)
//         router.push({name: 'Home'})
//       })
//       .catch(() => {
//         swal.fire ({
//           icon: 'error',
//           title: '로그인 실패',
//           text: '잘못된 아이디 또는 패스워드입니다.',
//           scrollbarPadding: false
//           })    
//       })
//     },

//     getUserInfo({commit}, username) {
//       axios({
//         method: 'GET',
//         //url: `URL + /accounts/${username}/get_user_info/`,
//         url: SERVER.URL + SERVER.ROUTES.accounts.default + String(username) + SERVER.ROUTES.accounts.getUserInfo,
//       })
//       .then(res => {
//         commit('GET_USER_INFO', res.data)
//       })
//       .catch(err => console.log(err))
//     },
//     getMyProfile: function ({ commit, state }) {
//       axios({
//         method: "GET",
//         //url: `${SERVER_URL}profile/`,
//         //route: SERVER.ROUTES.accounts.myProfileDetail
//         url: SERVER.URL + SERVER.ROUTES.accounts.myProfileDetail
//       })
//       .then((res) => {
//         const nickname = res.data.nickname
//         const introduction = res.data.introduction
//         var image = ''
//         if (res.data.image) {
//           //image = 'http://127.0.0.1:8000' + res.data.image     
//           image = SERVER.ROUTES.image + res.data.image       
//         } else {
//           image = state.image
//         }
//         commit("GET_MY_PROFILE", { nickname, introduction, image })
//       })
//     },
//     updateProfile: function ({ commit, getters, state }, credentials) {
//       axios({
//         method: "PUT",
//         //url: `${SERVER_URL}accounts/profile/`,
//         //route: SERVER.ROUTES.accounts.myProfileDetail,
//         url: SERVER.URL + SERVER.ROUTES.accounts.myProfileDetail,
//         data: credentials,
//         headers: getters.token,
//       })
//       .then((res) => {
//         // 대상 포함 여부
//         const nickname = res.data.nickname
//         const introduction = res.data.introduction
//         var image = ''
//         if (res.data.image) {
//           //image = 'http://127.0.0.1:8000' + res.data.image   
//           image = SERVER.ROUTES.image + res.data.image         // drf
//           //image = state.image // 스프링
//         } else {
//           image = state.image
//         }
//         commit("GET_MY_PROFILE", { nickname, introduction, image })        
//       })
//       .catch((err) => {console.log(err.response.data.error)})
//     },
//     logout({commit}) {
//       localStorage.removeItem('jwt')
//       commit('LOGOUT')
//       router.push({name: 'Home'})
//       window.location.reload();  // 로그아웃시 강제 새로고침 => 각종 버그 방지
//       // this.$router.go();
//       // this.$forceUpdate();
//     },
//     checkLogin({commit}, token) {
//       if (token) {
//         commit('LOGIN')
//       }
//     },
//     // MOVIES ACTIONS
//     getMovie({commit}, tokenId) {
//       axios({
//         method: 'GET',
//         //url: URL + '/movies/${tokenId.id}/',
//         url: SERVER.URL + SERVER.ROUTES.movies.movieDetail + String(tokenId.id) + '/',
//         headers: tokenId.token,
//       })
//       .then(res => {
//         commit('GET_MOVIE', res.data)
//       })
//       .catch(err => console.log(err))
//     },
//     getMovies({commit}, token) {
//       axios({
//         method: 'GET',
//         // '/movies/'
//         url: SERVER.URL + SERVER.ROUTES.movies.home,
//         headers: token,
//       })
//       .then(res => {
//         commit('GET_MOVIES', res.data)
//       })
//       .catch(err => console.log(err))
//     },
//     getMoviesRecommend({commit}, tokenId) {
//       axios({
//         method: 'GET',
//         //url: URL + '/movies/${tokenId.id}/recommend/',
//         url: SERVER.URL + '/movies/' + String(tokenId.id) + SERVER.ROUTES.movies.movieRecommend,
//         headers: tokenId.token,
//       })
//       .then(res => {
//         commit('GET_MOVIES_RECOMMEND', res.data)
//       })
//       .catch(err => console.log(err))
//     },

//   },
// })



export const useCounterStore = defineStore('counter', () => {
  const movies = ref([])
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })


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


  // 회원가입
  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  // 로그인
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
        router.push({ name: 'MainView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  // 로그아웃
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'MainView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }



  return { movies, API_URL, isLogin, token, getMovies, signUp, logIn, logOut }
}, { persist: true })

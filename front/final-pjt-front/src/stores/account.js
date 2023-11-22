import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useCounterStore = defineStore('account', () => {
  const accountStore = useCounterStore();
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const user = ref([])
  const loginUser = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const checkLoginUser = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/loginUser/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
      .then((res) =>{
        // console.log(res.data)
        loginUser.value = { id: res.data.userId, username: res.data.username }
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
        // // 회원가입 후에 자동으로 로그인 되도록.  
        // const password = password1
        // signUp_logIn({ username, password })
        
        // console.log(res.data)
        // token.value = res.data.key
        router.push({ name: 'MainView' })
      })
      .catch((err) => {
        console.log(err)
        alert('비밀번호가 일치하지 않습니다.')
      })
  }

  // 회원가입 후 자동 로그인 >> 영화 선택 페이지로 넘어가.
  // const signUp_logIn = function (payload) {
  //   const { username, password } = payload

  //   axios({
  //     method: 'post',
  //     url: `${API_URL}/accounts/login/`,
  //     data: {
  //       username, password
  //     }
  //   })
  //     .then((res) => {
  //       // console.log(res.data)
  //       token.value = res.data.key
  //       accountStore.checkLoginUser()
  //       router.push({ name: 'RecommendChoiceView' })
  //     })
  //     .catch((err) => {
  //       console.log(err)
  //       alert('아이디 또는 비밀번호가 일치하지 않습니다.')
  //     })
  // }

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
        // console.log(res)
        token.value = res.data.key
        accountStore.checkLoginUser()
        router.push({ name: 'MainView' })
      })
      .catch((err) => {
        console.log(err)
        alert('아이디 또는 비밀번호가 일치하지 않습니다.')
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
        loginUser.value = null
        router.push({ name: 'MainView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const findUser = function (userId) {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/${userId}/`,
    })
    .then((res) => {
        // console.log(res.data.username)
        user.value = res.data.username
      })
      .catch((err) => {
        console.log(err)
      })
  }
  return { API_URL, isLogin, token, user, loginUser,
    signUp, logIn, logOut, findUser, checkLoginUser,
  }
}, { persist: true })

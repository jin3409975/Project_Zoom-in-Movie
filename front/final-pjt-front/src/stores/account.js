import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'


export const useCounterStore = defineStore('account', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
    // return token.value !== null && token.value !== undefined
  })


  // 회원가입
  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }

    })
      .then((res) => {
        console.log(res.data)
        const password = password1
        logIn({ username, password })
        // 회원가입 후에 자동으로 로그인 되도록.  
        
        // token.value = res.data.key
        // router.push({ name: 'MainView' })
      })
      .catch((err) => {
        console.log(err)
        alert('비밀번호가 일치하지 않습니다.')
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
        router.push({ name: 'MainView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }



  return { API_URL, isLogin, token, signUp, logIn, logOut }
}, { persist: true })

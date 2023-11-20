<template>
    <div>
        <h1 class="loginText">로그인</h1>
        <form @submit.prevent="logIn" class="loginForm">
            <input type="text" v-model.trim="username" placeholder="아이디">
            <input type="password" v-model.trim="password" placeholder="비밀번호">
            <button type="submit">로그인</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const router = useRouter()
const username = ref(null)
const password = ref(null)

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
    try {
        // 로그인 API 호출
        store.logIn(payload)

        // 로그인 성공 시 메인 페이지로 이동
        // router.push({ name: 'MainView' })
    } catch (error) {
        console.error('로그인 에러:', error)
        // 실패 시 에러 처리 로직 추가
        alert('비밀번호가 일치하지 않습니다.')
    }
}

</script>

<style scoped>
.loginText {
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 0px;
    color: white;
}

.loginForm {
    display: flex;
    flex-direction: column;
}

.loginForm input {
  background-color: #ffffff;
  border: 1px solid #cccccc;
  width: 30vh;
  color: #000000;
  font-size: 16px;
  padding: 10px; /* 내부 여백을 조절하세요 */
  border-radius: 4px;
  margin-bottom: 10px; /* 입력란 간의 간격을 조절하세요 */
}

.loginForm input::placeholder {
    font-size: 12px; /* 플레이스홀더의 폰트 크기 */
    letter-spacing: -0.5px; /* 플레이스홀더의 글자 간격 */
    font-weight: 500;
    color: #BEBAB7; /* 플레이스홀더의 색상 및 투명도 */
    padding-left: 1vh;
}

.loginForm button {
    position: relative;
    background-color: rgb(248, 47, 98, 0.3);
    color: white; /* 텍스트 색상은 흰색 */
    font-weight: 700; /* 굵은 폰트 */
    text-align: center;
    letter-spacing: -0.1px;
    width: 100%;
    border-radius: 40px;
    font-size: 16px;
    height: 4.5vh;
    margin: 1.5vh 0;
    border: none; /* 테두리 없음 */
    outline: none;
    cursor: pointer;
    transition: background-color 0.3s; /* 마우스 호버 시 배경색 변경을 위한 트랜지션 */
}

.loginForm button:hover {
    background-color: rgba(255, 182, 193, 0.5); /* 페이스트 핑크색 */
}


</style>
<template>
    <div>
      <h1 class="signupText">회원가입</h1>
      <form @submit.prevent="registerUser" class="signupForm">
        <input type="text" placeholder="아이디" v-model="username">
        <input type="password" placeholder="비밀번호" v-model="password">
        <input type="password" placeholder="비밀번호 확인" v-model="confirmPassword">
        <button>회원가입</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const username = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  
  const registerUser = () => {
    if (password.value === confirmPassword.value) {
      // 비밀번호와 확인 비밀번호가 일치할 때 회원가입 로직을 실행합니다.
      // 여기에서 서버로 회원가입 요청을 보내는 코드를 작성하면 됩니다.
      // 서버 요청을 처리하는 방법은 백엔드 기술에 따라 다를 수 있습니다.
    } else {
      // 비밀번호와 확인 비밀번호가 일치하지 않을 때 에러 처리 로직을 추가할 수 있습니다.
      alert('비밀번호가 일치하지 않습니다.');
    }
  };
  </script>
  
  <style scoped>
  .signupText {
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 0px;
    color: white;
  }
  
  .signupForm {
    display: flex;
    flex-direction: column;
  }
  
  .signupForm input {
    background-color: #191A1C;
    border: 1px solid #E73E3E;
    width: 30vh;
    color: white;
    font-size: 16px;
    padding: 10px;
    border-radius: 4px;
    margin-bottom: 10px;
  }
  
  .signupForm input::placeholder {
    font-size: 12px;
    letter-spacing: -0.5px;
    font-weight: 500;
    color: #BEBAB7;
    padding-left: 1vh;
  }
  
  .signupForm button {
    position: relative;
    background-color: rgb(248, 47, 98, 0.3);
    color: white;
    font-weight: 700;
    text-align: center;
    letter-spacing: -0.1px;
    width: 100%;
    border-radius: 40px;
    font-size: 16px;
    height: 4.5vh;
    margin: 1.5vh 0;
    border: none;
    outline: none;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .signupForm button:hover {
    background-color: rgba(255, 182, 193, 0.5);
  }
  </style>
  
<template>
  <div class="app">
    <header>
      <nav class="nav">
        <div>
          <RouterLink :to="{ name: 'MainView' }">
            <img src="@/assets/logo.png" class="logo" alt="logo">
          </RouterLink>
          <RouterLink :to="{ name: 'MainView' }">Home</RouterLink>
          <RouterLink :to="{ name: 'CategoryView' }">category</RouterLink>
          <RouterLink :to="{ name: 'SignUpView' }">signup</RouterLink>
          <RouterLink :to="{ name: 'LoginView' }">login</RouterLink>
          <RouterLink :to="{ name: 'MovieDetailView' }">movie</RouterLink>
          <RouterLink :to="{ name: 'MyPageView' }">mypage</RouterLink>
          <RouterLink :to="{ name: 'RecommendChoiceView' }">choice</RouterLink>
          <RouterLink :to="{ name: 'RecommendView' }">recommend</RouterLink>
        </div>
        <ProFile/>
      </nav>
    </header>

    <RouterView class="router-view"/>
    <footer class='footer'>
      고객센터(이용 및 결제 문의)  ssafy10th@ssafy.com • 02-1234-5678 (유료) / 제휴 및 대외 협력  https://ssafy.com
      <br>
      주식회사 일단넘겨 / 대전광역시 유성구 덕명동 124 유성연수원 / 이용약관 / 개인정보 처리 방침 / 청소년 보호정책
    </footer>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import ProFile from './components/ProFile.vue';


</script>

<style>
.backSize {
  margin: 7% 0 0 0;
  height: 100%;
}
</style>

<style scoped>
.app {
  position: relative;
}
.logo {
  width: 80px;
}
.nav {
  background-color: #141414;
  color: white;
  height: 7vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10px;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.router-view {
  margin-top: 7vh;
  padding-bottom: 8vh;
}


nav a {
  font-family: Helvetica, sans-serif;
  color: white;
  text-decoration: none;
  margin: 0 15px;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
  color: #f5a623; /* 강조 색상 적용 */
}

.footer {
  position: absolute;
  box-sizing: border-box;
  padding: 0;
  color: #f2f2f2;
  text-align: center;
  padding: 20px 0;
  font-size: 14px;
  bottom: 0;
  width: 100%;
  height: 8vh;
  opacity: 0.5;
  background-color: transparent;
}
</style>
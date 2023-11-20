<template>
  <div class="app">
    <header>
      <nav class="nav">
        <div>
          <RouterLink :to="{ name: 'MainView' }"><img src="@/assets/logo.png" class="logo" alt="logo"></RouterLink>
          <RouterLink :to="{ name: 'RecommendView' }">나만의 영화추천</RouterLink>
          <div class="dropdown">
            <RouterLink :to="{ name: 'CategoryView' }" class="dropbtn">카테고리</RouterLink>
            <div class="dropdown-content">
              <a>액션</a>
              <a>드라마</a>
              <a>공포</a>
              <a>모험</a>
              <a>애니</a>
              <a>스릴러</a>
              <a>기타</a>
            </div>
          </div>
          <RouterLink :to="{ name: 'RecommendChoiceView' }">choice</RouterLink>
          <RouterLink :to="{ name: 'MovieDetailView' }">movie</RouterLink>
        </div>
        <div v-if="true">
          <RouterLink :to="{ name: 'MyPageView' }">mypage</RouterLink>
          <RouterLink :to="{ name: 'SignUpView' }">signup</RouterLink>
          <RouterLink :to="{ name: 'LoginView' }">login</RouterLink>
        </div>
        <div v-if="false">
          <ProFile/>
        </div>
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


<!-- 전역 스타일 -->
<style>
.commentProfile {
  width: 35px;
  height: 35px;
  border-radius: 100%;
  margin-right: 1.3%;
}

* {
  font-family: 'Roboto', sans-serif;
  word-break: keep-all;
}

hr {
  margin: 0 auto;
  border-color: white;
  width: 90%;
}

.backSize {
  margin: 7vh 0 0;
  height: 100%;
  min-height: 93vh;
  padding: 0 3.5%;
}

.midDisplay {
  display: flex;
  flex-direction: column;
  align-items: center;
}

/* 메인 백그라운드 설정 */
.mainBackColor {
  background-color: #141414;
}

.listTitle {
  color: white;
  font-size: 2em;
  font-weight: bold;
  margin: 0;
  padding: 30px 30px 0 0;
}

.movieList {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: flex-start;
  gap: 20px;
  padding: 20px 0;
}

.max_w1000 {
  max-width: 1000px;
}

.marginMid {
  margin: 0 auto;
}

</style>

<!-- 스코프 스타일 -->
<style scoped>
/* 애플리케이션 레이아웃 설정 */
.app {
  position: relative;
}

/* 로고 크기 설정 */
.logo {
  width: 80px;
}

/* 네비게이션 바 스타일 설정 */
.nav {
  background-color: #141414;
  height: 7vh;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 10px;
  padding-left: 3.5%;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* 네비게이션 내부 div 설정 */
nav div {
  height: 100%;
  display: flex;
  align-items: center;
}

/* 네비게이션 링크 스타일 설정 */
nav div a {
  display: block;
  font-family: Helvetica, sans-serif;
  color: white;
  text-decoration: none;
  margin: 0 15px;
  font-weight: bold;
}

/* 링크 호버 효과 */
nav a:hover {
  text-decoration: underline;
  color: #f5a623;
}

/* 드롭다운 메뉴 스타일 */
.dropdown {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 드롭다운 메뉴 내용 */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #212121;
  height: auto;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  top: 100%;
  left: 0;
}

/* 드롭다운 메뉴 링크 스타일 */
.dropdown-content a {
  color: #b6b6b6;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

/* 드롭다운 메뉴 링크 호버 효과 */
.dropdown-content a:hover {
  background-color: #2D2D2D;
  opacity: 1;
  color: white;
  margin: 0;
}

/* 드롭다운 활성화시 내용 표시 */
.dropdown:hover .dropdown-content {
  display: block;
}

/* 라우터 뷰 마진 설정 */
.router-view {
  margin-top: 7vh;
  padding-bottom: 8vh;
}

/* 푸터 스타일 설정 */
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
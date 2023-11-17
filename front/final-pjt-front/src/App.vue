<template>
  <div>
    <header>
      <nav class="nav">
        <RouterLink :to="{ name: 'MainView' }">Main</RouterLink>
      |
        <RouterLink :to="{ name: 'CategoryView' }">category</RouterLink>
      |
        <RouterLink :to="{ name: 'LoginSignUpView' }">account</RouterLink>
      |
        <RouterLink :to="{ name: 'MovieDetailView' }">movie</RouterLink>
      |
        <RouterLink :to="{ name: 'MyPageView' }">mypage</RouterLink>
      |
        <RouterLink :to="{ name: 'RecommendChoiceView' }">choice</RouterLink>
      |
        <RouterLink :to="{ name: 'RecommendView' }">recommend</RouterLink>

      <ProFile/>
      </nav>
    </header>

    <RouterView class="router-view"/>

    <footer class='footer'>
      팀명: 일단 넘겨, 맏이: 이지은(아이유), 막내: 차현철(박항서)
    </footer>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import ProFile from './components/ProFile.vue';


</script>

<style scoped>
.nav {
  background-color: #333; /* 나브바의 배경색 */
  color: white; /* 나브바 내 텍스트 색상 */
  height: 50px; /* 나브바의 높이 */
  display: flex; /* 플렉스박스 레이아웃 사용 */
  justify-content: space-between; /* 요소들을 양 끝에 배치 */
  align-items: center; /* 세로 방향에서 중앙 정렬 */
  padding: 0 10px; /* 양옆 패딩 */
  position: fixed; /* 고정 위치 */
  top: 0; /* 상단에 위치 */
  left: 0; /* 왼쪽에서 시작 */
  width: 100%; /* 전체 너비 */
  z-index: 1000; /* 다른 요소들보다 상위에 위치 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
}

.router-view {
  margin-top: 50px; /* 상단 나브바 높이에 맞춤 */
  margin-bottom: 50px; /* 하단 푸터 높이에 맞춤 */
}


nav a {
  color: white; /* 링크 텍스트 색상 */
  text-decoration: none; /* 밑줄 없애기 */
  margin: 0 15px; /* 링크 간격 */
}

nav a:hover {
  text-decoration: underline; /* 마우스 오버시 밑줄 */
}

.footer {
  background-color: #f2f2f2; /* 푸터의 배경색 */
  color: #333; /* 텍스트 색상 */
  text-align: center; /* 텍스트를 중앙 정렬 */
  padding: 20px 0; /* 상하 패딩 */
  font-size: 14px; /* 폰트 크기 */
  border-top: 1px solid #e7e7e7; /* 상단 테두리 */
  position: fixed; /* 필요에 따라 위치 조정 */
  bottom: 0; /* 페이지 하단에 고정 */
  width: 100%; /* 너비 */
}
</style>
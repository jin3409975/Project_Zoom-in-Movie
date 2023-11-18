<template>
  <div>
    <header>
      <nav class="nav">
        <RouterLink :to="{ name: 'MainView' }">Main</RouterLink>
      |
        <RouterLink :to="{ name: 'CategoryView' }">category</RouterLink>
      |
        <RouterLink :to="{ name: 'SignUpView' }">signup</RouterLink>
      |
        <RouterLink :to="{ name: 'LoginView' }">login</RouterLink>
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
      고객센터(이용 및 결제 문의)  ssafy10th@ssafy.com • 02-515-9985 (유료) / 제휴 및 대외 협력  https://watcha.team/contact
      주식회사 왓챠 / 대표 박태훈 / 서울특별시 서초구 강남대로 343 신덕빌딩 3층 / 사업자등록번호 211-88-66013 / 통신판매업 신고번호 제 2019-서울서초-0965호 / 호스팅 서비스 제공자 아마존웹서비시즈코리아 유한회사 / 대표번호 02-515-9985 / 이용약관 / 개인정보 처리 방침 / 청소년 보호정책
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
  height: 7vh; /* 나브바의 높이 */
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
  margin-top: 7vh; /* 상단 나브바 높이에 맞춤 */
  /* margin-bottom: 50px; */
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
  color: #f2f2f2;
  text-align: center;
  padding: 20px 0;
  font-size: 14px;
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 8vh;
  z-index: 999;
}
</style>
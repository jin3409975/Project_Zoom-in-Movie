<template>
  <div class="app">
    <header>
      <nav class="nav" :class="{ 'nav-hidden': !navVisible }">
        <div>
          <RouterLink :to="{ name: 'MainView' }"><img src="@/assets/logo.png" class="logo" alt="logo"></RouterLink>
          <RouterLink :to="{ name: 'RecommendView' }">나만의 영화추천</RouterLink>
          <div class="dropdown">
            <p class="dropbtn">카테고리</p>
            <div class="dropdown-content">
              <RouterLink
               v-for="genre in movieStore.genres"
               :key="genre.genre_id"
               :to="{ name: 'CategoryView', params: {genre: genre.genre_name} }">
               {{ genre.genre_name }}
              </RouterLink>
            </div>
          </div>
        </div>
        <!-- 로그인 상태에서 보이는 메뉴 -->
        <div v-if="store.isLogin">
          <a href="#" onclick="alert('준비 중입니다.')">My Page</a>
          <a href="#" @click.prevent="store.logOut">logout</a>
        </div>
        <!-- 로그아웃 상태에서 보이는 메뉴 -->
        <div v-else>
          <RouterLink :to="{ name: 'SignUpView' }">signup</RouterLink>
          <RouterLink :to="{ name: 'LoginView' }">login</RouterLink>
        </div>
      </nav>
    </header>

    <RouterView class="router-view"/>

  </div>
</template>

<script setup>
import { onMounted, onUnmounted, ref, watchEffect  } from 'vue';
import { useMovieStore } from '@/stores/movie.js'
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/account.js'

const store = useCounterStore()
const movieStore = useMovieStore()

watchEffect(() => {
  if (movieStore.popularMovies.length < 1) {
    movieStore.getPopularMovies()
  }
  if (movieStore.genres.length < 2) {
    movieStore.getGenres()
  }
})

// nav bar 스크롤 내리면 사라지고 살짝 올리면 나타나게
const navVisible = ref(true);
let lastScrollTop = 0; // 마지막 스크롤 위치를 저장할 변수

const handleScroll = () => {
  const st = window.pageYOffset || document.documentElement.pageYOffset;

  if (st > lastScrollTop) {
    // 아래로 스크롤
    navVisible.value = false;
  } else {
    // 위로 스크롤
    navVisible.value = true;
  }
  lastScrollTop = st <= 0 ? 0 : st; // 음수가 되지 않도록
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});

</script>


<!-- 전역 스타일 -->
<style>
.nav-hidden {
  transform: translateY(-100%); 
  /* transition: transform 0.3s ease-in-out;  */
}

.sticky {
  position: sticky !important;
  top: 0;
}

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

.side-padding-zero-important {
  padding-left: 0 !important;
  padding-right: 0 !important;
}

hr {
  margin: 0 auto;
  border-color: white;
  width: 90%;
}

.backSize {
  margin: 7v 0 0 0;
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
  margin-left: 1.5%;
}

.movieList {
  display: flex;
  flex-wrap: wrap;
  margin-top: 15px;
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
  transition: transform 0.3s ease-in-out;
}

/* 네비게이션 내부 div 설정 */
nav div {
  height: 100%;
  display: flex;
  align-items: center;
}

/* 네비게이션 링크 스타일 설정 */
nav div a, nav div p {
  display: block;
  font-family: Helvetica, sans-serif;
  color: white;
  text-decoration: none;
  margin: 0 15px;
  font-weight: bold;
}

nav div p:hover {
  color: #f5a623;
  cursor: pointer;
}

/* 링크 호버 효과 */
nav a:hover {
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
}



</style>
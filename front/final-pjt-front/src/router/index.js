import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import CategoryView from '@/views/CategoryView.vue'
import SignUpView from '@/views/SignUpView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import LoginView from '@/views/LoginView.vue'
import MyPageView from '@/views/MyPageView.vue'
import RecommendChoiceView from '@/views/RecommendChoiceView.vue'
import RecommendView from '@/views/RecommendView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView
    },
    {
      path: '/category/:genre',
      name: 'CategoryView',
      component: CategoryView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView
    },
    {
      path: '/movie/:movieId',
      name: 'MovieDetailView',
      component: MovieDetailView
    },
    // {
    //   path: '/mypage',
    //   name: 'MyPageView',
    //   component: MyPageView
    // },
    // {
    //   path: '/choice',
    //   name: 'RecommendChoiceView',
    //   component: RecommendChoiceView
    // },
    {
      path: '/recommend',
      name: 'RecommendView',
      component: RecommendView
    },
  ],
  scrollBehavior() {
    // 페이지 전환 시 스크롤을 맨 위로 이동
    return { top: 0 }
  }
})


import { useCounterStore } from '@/stores/account'

router.beforeEach((to, from) => {
  const store = useCounterStore()
  if ((to.name === 'CategoryView'||
    to.name === 'RecommendView'||
    to.name === 'MovieDetailView') && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LoginView' }
  }
  if ((to.name === 'SignUpView' || to.name === 'LoginView') && (store.isLogin)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'MainView' }
  }
})

export default router

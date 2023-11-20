import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import CategoryView from '@/views/CategoryView.vue'
import SignUpView from '@/views/SignUpView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
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
      path: '/category',
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
      path: '/logout',
      name: 'LogoutView',
      component: LogoutView
    },
    {
      path: '/movie',
      name: 'MovieDetailView',
      component: MovieDetailView
    },
    {
      path: '/mypage',
      name: 'MyPageView',
      component: MyPageView
    },
    {
      path: '/choice',
      name: 'RecommendChoiceView',
      component: RecommendChoiceView
    },
    {
      path: '/recommend',
      name: 'RecommendView',
      component: RecommendView
    },
  ]
})

export default router

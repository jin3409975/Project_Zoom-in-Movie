import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import CategoryView from '@/views/CategoryView.vue'
import LoginSignUpView from '@/views/LoginSignUpView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
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
      path: '/account',
      name: 'LoginSignUpView',
      component: LoginSignUpView
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

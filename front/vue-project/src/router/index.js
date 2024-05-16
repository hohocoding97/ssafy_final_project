import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import SignUpView from '@/views/SignUpView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/:movie_id/',
      name: 'movieDetail',
      component : MovieDetailView,
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
  ]
})

export default router

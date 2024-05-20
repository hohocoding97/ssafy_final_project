import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import EditProfileView from '@/views/EditProfileView.vue'
import Test from '@/views/Test.vue'
import CommunityView from '@/views/CommunityView.vue'
import WriteView from '@/views/WriteView.vue'
import BoardView from '@/views/BoardView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/:movieId/',
      name: 'movieDetail',
      component : MovieDetailView,
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
      path: '/profile/edit',
      name: 'EditProfileView',
      component: EditProfileView
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/write',
      name: 'write',
      component: WriteView
    },
    {
      path: '/board',
      name: 'board',
      component: BoardView
    }
  ]
})

export default router

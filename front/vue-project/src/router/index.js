import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import EditProfileView from '@/views/EditProfileView.vue'
import GenreMoviesView from '@/views/GenreMoviesView.vue'
import Test from '@/views/Test.vue'
import CommunityView from '@/views/CommunityView.vue'
import WriteView from '@/views/WriteView.vue'
import articleDetailView from '@/views/articleDetailView.vue'
import EditArticleView from '@/views/EditArticleView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SearchResultViews from '@/views/SearchResultView.vue'

import { useCounterStore } from '@/stores/userCounter'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/:movieId',
      name: 'movieDetail',
      component : MovieDetailView,
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView,
      beforeEnter: (to, from) => {
        if (useCounterStore().is_login) return { name : 'home'}//이미 로그인 했으면 회원가입 페이지 가지 말기
      }
    },
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (useCounterStore().is_login) return { name : 'home'} //이미 로그인 했으면 로그인 페이지 가지 말기
      }
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
      path: '/genre/:genre_code',
      name: 'genre_movies',
      component: GenreMoviesView,
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/write',
      name: 'write',
      component: WriteView,
      beforeEnter: (to, from) => {
        if (!useCounterStore().is_login) return { name : 'home'} //이미 로그인 안했으면 작성페이지 못가게하기
      }
    },
    {
      path: '/articleDetail/:articleId',
      name: 'articleDetail',
      component: articleDetailView
    },
    {
      path:'/profile/:userId',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/edit/:articleId',
      name : 'editArticle',
      component: EditArticleView
    },
    {
      path: '/search/:query',
      name : 'search',
      component : SearchResultViews,
    }
    
  ]
})

export default router

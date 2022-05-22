import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/accounts/LoginView'
import LogoutView from '@/views/accounts/LogoutView'
import NotFound404 from '@/views/accounts/NotFound404'
import SignupView from '@/views/accounts/SignupView'
import ProfileView from '@/views/accounts/ProfileView'

import CommnuityView from '@/views/community/CommunityView'
import ReviewNewView from '@/views/community/ReviewNewView'
import ReviewDetailView from '@/views/community/ReviewDetailView'
import ReviewEditView from '@/views/community/ReviewEditView'

import RecommendView from '@/views/RecommendView'

import MovieDetailView from '@/views/movies/MovieDetailView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  // ---------accounts------------
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
  },
  // ---------community------------
  {
    path: '/community',
    name: 'community',
    component: CommnuityView
  },
  {
    path: '/community/create',
    name: 'create',
    component: ReviewNewView
  },
  {
    path: '/community/:reviewPk',
    name: 'reviewDatail',
    component: ReviewDetailView
  },
  {
    path: '/community/:reviewPk/edit',
    name: 'reviewEdit',
    component: ReviewEditView
  },
    // ---------recommend------------
  {
    path: '/recommend/:username',
    name: 'recommend',
    component: RecommendView
  },
    // ---------recommend------------
    {
      path: '/movies/:moviePk',
      name: 'movieDetail',
      component: MovieDetailView
    },
  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },
  // ---------404------------
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/404',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
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

// 추가
import MovieAllView from '@/views/movies/MovieAllView'

import RecommendHomeView from '@/views/recommend/RecommendHomeView'
import RecommendView from '@/views/recommend/RecommendView'

import MovieDetailView from '@/views/movies/MovieDetailView'
import store from '@/store'
import bus from '@/utils/bus'
import swal from 'sweetalert'

// import store from '@/store/index'

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
          // next를 호출해야만 호출됨.
    beforeEnter: (to, from, next) => {
      to, from, next
      return store.dispatch('fetchCurrentUser')
        .then(() => {
            return store.dispatch('fetchProfile', store.getters.currentUser.username)
              .then(() => {
                store.dispatch('getRecommends')
                next()})
        })
    }
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
    path: '/community/create/:movieTitle',
    name: 'reviewcreate',
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
    path: '/recommend/',
    name: 'recommend',
    component: RecommendHomeView,
    beforeEnter: (to, from, next) => {
      to, from
      bus.$emit('start:spinner')
      return store.dispatch('fetchCurrentUser')
        .then(() => {
          return store.dispatch('getRecommends')
        })
          .then(() => {next()})
    }
  },
  {
    path: '/recommend/:username',
    name: 'algorecommend',
    component: RecommendView
  },
  // ---------movie detail------------
  {
    path: '/movies/:moviePk',
    name: 'movieDetail',
    component: MovieDetailView,
    beforeEnter: (to, from, next) => {
      to, from, next
      return store.dispatch('fetchCurrentUser')
        .then(() => {
            console.log('fetchuser받음 2');
            console.log(store.getters.currentUser.username, '2');
            return store.dispatch('fetchProfile', store.getters.currentUser.username)
              .then(() => {
                next()})
          })
      }
    },
  // ------- movielist ------------
  {
    path: '/movies/',
    name: 'movieAll',
    component: MovieAllView,
    beforeEnter: (to, from, next) => {
      to, from
      bus.$emit('start:spinner')
      return store.dispatch('getAllMovies')
        .then(() => {next()})
    }
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
    component: NotFound404,
    beforeEnter: () => {
      swal('잘못된 경로입니다.', '다시 확인해주세요')
      router.replace('')
    }
  },
  {
    path: '*',
    beforeEnter: () => {
      swal('잘못된 경로입니다.', '다시 확인해주세요')
      router.replace('')
    }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})



export default router
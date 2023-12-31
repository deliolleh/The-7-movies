import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import store from '@/store'
import swal from 'sweetalert';

export default {

  state: {
    token: localStorage.getItem('token') || '',
    currentUser: {},
    profile: {},
    authError: null,
    valid: null,
  },

  getters: {
    isLoggedIn: state => !!state.token,
    currentUser: state => state.currentUser,
    profile: state => state.profile,
    authError: state => state.authError,
    authHeader: state => ({ Authorization: `Token ${state.token}` }),
    isValid: state => state.valid,
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => {
      state.currentUser = user
    },
    SET_PROFILE: (state, profile) => {
      state.profile = profile
    },
    SET_AUTH_ERROR: (state, error) => state.authError = error,
    SCORE_UPDATE: (state, profile) => {
      state.profile = profile
    }
  },
  actions: {
    fetchProfile({ commit, getters }, username) {
      /*
      GET: profile URL로 요청보내기
        성공하면
          state.profile에 저장
      */
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
        .catch(() => {
          console.log('프로필 들고 올수 없음.');
        })
    },
    saveToken({ commit }, token) {
      /* 
      state.token 추가 
      localStorage에 token 추가
      */
      commit('SET_TOKEN', token)
      localStorage.setItem('token', token)
    },

    removeToken({ commit }) {
      /* 
      state.token 삭제
      localStorage에 token 추가
      */
      commit('SET_TOKEN', '')
      console.log(1)
      localStorage.setItem('token', '')
    },

    login({ commit, dispatch }, credentials) {
      /* 
      POST: 사용자 입력정보를 login URL로 보내기
        성공하면
          응답 토큰 저장
          현재 사용자 정보 받기
          메인 페이지로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({ name: 'home' })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    signup({ commit, dispatch, getters }, credentials) {
      /* 
      POST: 사용자 입력정보를 signup URL로 보내기
        성공하면
          응답 토큰 저장
          현재 사용자 정보 받기
          메인 페이지(ArticleListView)로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.signup(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          console.log(credentials)
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          axios({
            url: drf.accounts.init(),
            method: 'get',
            headers: getters.authHeader
          })
            .then(() => {
              router.push({ name: 'algorecommend', params: { username: credentials.username } })
            })
        })
        .catch(err => {
          console.error(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
        })
    },

    logout({ getters, dispatch, commit }) {
      /* 
      POST: token을 logout URL로 보내기
        성공하면
          토큰 삭제
          사용자 알람
          LoginView로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        // data: {},
        headers: getters.authHeader,
      })
        .then(() => {
          dispatch('removeToken')
          commit('SET_AUTH_ERROR', null)
          commit('SET_PROFILE', {})
          commit('SET_CURRENT_USER', {})
          swal('로그아웃 되었습니다.', '서비스를 이용하시려면 로그인해주세요!')
          router.push('/login')
        })
        .error(err => {
          console.error(err.response)
        })
    },

    async fetchCurrentUser({ commit, getters, dispatch }) {
      /*
      GET: 사용자가 로그인 했다면(토큰이 있다면)
        currentUserInfo URL로 요청보내기
          성공하면
            state.cuurentUser에 저장
          실패하면(토큰이 잘못되었다면)
            기존 토큰 삭제
            LoginView로 이동
      */
      if (getters.isLoggedIn) {
        await axios({
          url: drf.accounts.currentUserInfo(),
          method: 'get',
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_CURRENT_USER', res.data)
            return res
          })
          .catch(err => {
            if (err.response.status === 401) {
              dispatch('removeToken')
              router.push({ name: 'login' })
            }
          })
      }
    },

    scoreCreate({ commit, getters }, profile) {
      return axios({
        url: drf.accounts.changeUserInfo(),
        method: 'put',
        headers: getters.authHeader,
        data: profile.genre_score_set
      })
        .then(res => {
          console.log(profile);
          commit('SCORE_UPDATE', res.data)
        })
        .then(() => {
          return store.dispatch('getRecommends')
        })
        .catch((err) => console.log(err, '에러발생'))
    },
    scoreUpdate({ commit, getters }, { profile, moviePk }) {
      return axios({
        url: drf.accounts.changeScoreInfo(moviePk),
        method: 'post',
        headers: getters.authHeader,
        data: profile.score_set
      })
        .then(res => {
          commit('SCORE_UPDATE', res.data)
        })
        .catch(() => console.log('생성에러'))
    },
    resetScore({ commit, getters }, { profile, moviePk }) {
      axios({
        url: drf.accounts.changeScoreInfo(moviePk),
        method: 'delete',
        headers: getters.authHeader,
        data: profile.genre_score_set
      })
        .then(res => {
          commit('SCORE_UPDATE', res.data)
          store.dispatch('getRecommends')
        })
        .catch(() => console.log('에러발생'))
    },
  },
}
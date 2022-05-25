// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
    searchMovies: [],
    movies: [], //전체
    movie: {}, // detail
    currentMovie: null, //pk
    recommend: [], // 추천용
    bestmovie: [],
    recommends: [], // 추천 받은 것
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    movies: state => state.movies,
    searchMovies: state => state.searchMovies,
    currentMovie: state => state.currentMovie,
    recommend: state => state.recommend,
    movie: state => state.movie,
    bestmovie: state => state.bestmovie,
    recommends: state => state.recommends
  },

  mutations: {
    GET_MOIVE_ALL: (state, movies) => state.movies = movies,
    GET_ALL_MOVIES: (state, movies) => state.searchMovies = movies,
    GET_MOVIE: (state, movie) => state.movie = movie,
    GET_MOIVE_PK: (state, pk) => state.currentMovie = pk,
    GET_RECOMMEND: (state, recommend) => state.recommend = recommend,
    GET_BEST_MOVIE: (state, movies) => state.bestmovie = movies,
    GET_RECOMMENDS: (state, movies) => state.recommends = movies
  },

  actions: {
    getMoviePk({ commit }, pk) {
      commit('GET_MOIVE_PK', pk)
    },
    getAllMovies({ commit, getters }) {
      axios({
        url: drf.movies.search(),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          commit('GET_ALL_MOVIES', res.data)
        })
        .catch(err => console.log(err))
    },
    getMoviesList({ commit, getters }) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.headers
      })
        .then(res => {
          console.log(res.data)
          commit('GET_MOIVE_ALL', res.data)
        })
        .catch(err => console.log(err))
    },
    getRecommend({commit, getters}) {
      axios({
        url: drf.movies.recommend(),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          commit('GET_RECOMMEND', res.data)

        })
    },
    getMovie({commit, getters}, moviePk) {
      return axios({
        url: drf.movies.detail(moviePk),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          commit('GET_MOVIE', res.data)
        })
    },
    getBestMovie({commit}) {
      axios({
        url: drf.movies.best(),
        method: 'get',
      })
        .then(res => {
          commit('GET_BEST_MOVIE', res.data)
        })
        .catch(() => console.log('메인 영화 안나옴'))
    },
    getRecommends({commit, getters}) {
      return axios({
        url: drf.movies.recommends(),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => {
          console.log('get recommends 실행?');
          commit('GET_RECOMMENDS', res.data)
          return res
        })
    }
  }
}

// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'


export default {
  // namespaced: true,

  // state는 직접 접근하지 않겠다!
  state: {
    searchMovies: [],
    movies: [],
    movie: [],
  },
  // 모든 state는 getters 를 통해서 접근하겠다.
  getters: {
    searchMovies: state => state.searchMovies
  },

  mutations: {
    GET_ALL_MOVIES: (state, movies) => state.searchMovies = movies
  },

  actions: {
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
    }
  }
}

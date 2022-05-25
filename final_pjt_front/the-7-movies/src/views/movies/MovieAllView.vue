<template>
  <v-app>
    <v-container>
      <v-row dense>
        <v-col
          cols="3"
          v-for="(movie, idx) in movies"
          :key="idx"
          >
          <v-hover
                    v-slot="{ hover }"
                    open-delay="200"
                  >
            <v-card
              :elevation="hover ? 16 : 2"
              width=300
              height=350
              :class="{ 'on-hover': hover }"
              >
              <router-link
                :to="{ name: 'movieDetail', params:{ moviePk: movie.pk} }">
                <v-img
                  :src="movie.poster_path"
                  height=350
                  ></v-img>
              </router-link>
            </v-card>
          </v-hover>
        </v-col>
      </v-row>
    </v-container>
    <infinite-loading @infinite="infiniteHandler"></infinite-loading>
  </v-app>
</template>

<script>
import InfiniteLoading from "vue-infinite-loading"
import { mapActions, mapGetters } from 'vuex'
import drf from '@/api/drf'
import axios from 'axios'
export default {
  name: 'MovieAllView',
  data () {
    return {
      currentPage: 1,
      
    }
  },
  components: {
    InfiniteLoading,
  },
  computed: {
    ...mapGetters(['movies']),
  },
  methods: {
    ...mapActions(['getMoviesList', 'getMoviesPage']),
    infiniteHandler($state) {
      this.currentPage += 1
      axios({
        url: drf.movies.paginator(this.currentPage),
        method: 'get',
        headers: this.$store.getters.headers
      })
        .then(res => {
          console.log(res.data)
          res.data.forEach((movie) => {
            this.$store.commit('GET_MOVIE_LIST', movie)
          })
          if (res.data.length) {
            $state.loaded()
          } else {
            $state.complete()
          }
        })
    }
  },
  created () {
    // this.getMoviesList()
    this.getMoviesPage(this.currentPage)
    // this.currentPage++
  }
}
</script>

<style>

</style>
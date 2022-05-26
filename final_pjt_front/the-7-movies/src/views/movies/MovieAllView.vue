<template>
  <v-app>
    <h1 class="text-center mt-10">
      <i class="fa-solid fa-video"></i> Movies
    </h1>
      <v-row
        class="mx-5"
      >
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
              :class="{ 'on-hover': hover }"
              >
              <router-link
                :to="{ name: 'movieDetail', params:{ moviePk: movie.pk} }">
                <v-img 
                  :src="movie.poster_path"
                  ></v-img>
              </router-link>
                  <v-card-title class="subtitle-2">{{movie.title}}</v-card-title>
                  <v-card-text>
          <v-row align="center" class="mx-0">
              <v-rating :value="movie.vote_score / 2" color="amber" dense half-increments readonly size="14">
              </v-rating>
              <div class="grey--text ml-4">
                  {{movie.release_date}}
              </div>
          </v-row>
          <div class="my-4 subtitle-2">
              <span v-for="(genre, idx) in movie.genres" :key="idx">
                  {{ genre.name }}
              </span>
          </div>
      </v-card-text>
            </v-card>
    </v-hover>
        </v-col>
      </v-row>
    <infinite-loading @infinite="infiniteHandler"></infinite-loading>
  </v-app>
</template>

<script>
import InfiniteLoading from "vue-infinite-loading"
import { mapActions, mapGetters } from 'vuex'
import drf from '@/api/drf'
import axios from 'axios'
import bus from '@/utils/bus'

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
    // this.currentPage++
  },
  mounted () {
    this.getMoviesPage(this.currentPage)
    window.scrollTo(0, 0)
    bus.$emit('end:spinner')
  }
}
</script>

<style>

</style>
<template>
  <v-app>
    <v-container>
      <v-row dense>
        <v-col
          cols="3"
          v-for="(movie, idx) in movies"
          :key="idx"
          >
      <v-card
        width=300
        height=350
        >
        <router-link
          :to="{ name: 'movieDetail', params:{ moviePk: movie.pk} }">
          <v-img
            :src="movie.poster_path"
            height=350
            ></v-img>
        </router-link>
        </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieAllView',
  computed: {
    ...mapGetters(['movies']),
  },
  methods: {
    ...mapActions(['getMoviesList']),
  },
  created () {
    this.getMoviesList()
  }
}
</script>

<style>

</style>
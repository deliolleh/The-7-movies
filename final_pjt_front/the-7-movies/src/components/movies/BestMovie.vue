<template>
  <v-app >
    <v-carousel hide-delimiters width="100%" height="auto">
      <v-carousel-item
        v-for="(item,i) in bestmovie"
        :key="i"
        width="100%"
      >
      <router-link :to="{ name: 'movieDetail', params: { moviePk: item.pk } }">
        <v-img
          :src="item.backdrop_path"
          width="100%"></v-img>
      </router-link>
      </v-carousel-item>
    </v-carousel>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'BestMovie',
  computed: {
    ...mapGetters(['bestmovie'])
  },
  methods: {
    ...mapActions(['getBestMovie'])
  },
  created() {
    this.getBestMovie()
  }
}
</script>

<style>

</style>
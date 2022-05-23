<template>
  <v-app>
    <v-carousel hide-delimiters>
      <v-carousel-item
        v-for="(item,i) in bestmovie"
        :key="i"
        :src="item.poster_path"
        width="1000"
        height="auto"
      >
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
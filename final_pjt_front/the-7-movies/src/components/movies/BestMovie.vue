<template>
  <v-carousel hide-delimiters>
    <v-carousel-item
      v-for="(item,i) in bestmovie"
      :key="i"
      :src="item.poster_path"
    >
    </v-carousel-item>
  </v-carousel>
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
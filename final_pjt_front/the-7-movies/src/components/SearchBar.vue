<template>
  <div>
    <input type="text" v-model="input">
    <div>
      <li v-for="(movie, idx) in searchMovies" :key="idx">
        {{ movie.title }}
      </li>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SearchBar',
  data() {
    return {
      input:''
    }
  },
  computed: {
    ...mapGetters(['searchMovies'])
  },
  methods: {
    ...mapActions(['getAllMovies'])
  },
  created() {
    this.getAllMovies()
  }
}

</script>

<style>

</style>
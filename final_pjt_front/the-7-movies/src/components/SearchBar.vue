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
    findItems () {
      if (this.input) {
        return this.searchMovies.filter((value) => {
          return value.indexOf(this.input) > -1
        })
      } else {
        return null
      }
    },
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
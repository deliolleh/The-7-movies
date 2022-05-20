<template>
  <div>
    <v-form>
      <v-text-field type="input" 
        v-model="input"
        label="영화 제목을 찾아주세요"
        hide-details="auto"
        >
      </v-text-field>
    </v-form>
    <select multiple
      @change="selectClick"
    >
      <option 
        v-for="(item, idx) in findItems" :key="idx"
        :input="item.title"
        >
          {{item.title}}
      </option>
    </select>
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
  methods: {
    selectClick(event) {
      this.input = event.target.value
      const selectedMovie = this.searchMovies.filter((value) => {
        return (value.title === event.target.value)
      })
      const payload = selectedMovie[0].pk
      this.getMoviePk(payload)
    },
    ...mapActions(['getAllMovies', 'getMoviePk']),
  },
  computed: {
    findItems () {
      if (this.input) {
        return this.searchMovies.filter((value) => {
          return (value.title.indexOf(this.input) > -1)
        }, this)
      } else {
        return null
      }
    },
    ...mapGetters(['searchMovies', 'currentMovie'])
  },
  created() {
    this.getAllMovies()
  }
}

</script>

<style>

</style>
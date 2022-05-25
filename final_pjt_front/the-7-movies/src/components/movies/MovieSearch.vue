<template>
  <div>
    <v-form @submit.prevent="search">
      <v-autocomplete 
        type="input" 
        :items="getTitle"
        label="영화 제목을 찾아주세요"
        hide-details="auto"
        @change="selectClick"
        >
      </v-autocomplete>
    </v-form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieSearch',
  data() {
    return {
      input:'',
    }
  },
  props: {
    movies: Array,
  },
  methods: {
    ...mapActions(['getMoviePk']),
    selectClick(event) {
      this.input = event.target.value
    },
    search(event) {
      console.log(event.target[0].value);
      this.$emit()
    }
  },
  computed: {
    getTitle() {
      const title = this.movies.map(object => {
        return object.title
      });
      return title
    },
    filteredList() {
      return this.movies.filter(object => {
        return object.title.includes(this.input)
      })
    },
    ...mapGetters(['searchMovies', 'currentMovie'])
  },
}

</script>

<style>

</style>
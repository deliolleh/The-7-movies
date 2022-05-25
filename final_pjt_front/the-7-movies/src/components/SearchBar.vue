<template>
  <div>
    <v-form>
      <v-autocomplete type="input" 
        v-model="input"
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
  name: 'SearchBar',
  data() {
    return {
      input:''||this.movietitle
    }
  },
  props: {
    movietitle: String,
  },
  methods: {
    ...mapActions(['getAllMovies', 'getMoviePk']),
    selectClick(event) {
      console.log(event);
      this.input = event
      const selectedMovie = this.searchMovies.filter((value) => {
        return (value.title === event)
      })
      const payload = selectedMovie[0].pk
      this.getMoviePk(payload)
    },
    onSubmit () {
        this.$emit('onSubmit', this.findItems[0].pk)
      },
  },
  computed: {
    getTitle() {
      const title = this.searchMovies.map(object => {
        return object.title
      });
      return title
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
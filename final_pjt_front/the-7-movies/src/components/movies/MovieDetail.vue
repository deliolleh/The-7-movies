<template>
  <div>
  <div class="text-center">
    <v-rating
      v-model="rating"
      icon-label="custom icon label text {0} of {1}"
    ></v-rating>
    {{ this.movie.title }}
  </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieDetail',
  data() {
    return {
      rating: 0,
    }
  },
  props: {
    username: String,
  },
  computed: {
    ...mapGetters(['movie', 'currentUser', 'profile']),
    
  },
  methods: {
    ...mapActions(['getMovie', 'scoreUpdate', 'fetchProfile', 'fetchCurrentUser']),
  },
  created() {
    this.getMovie(this.$route.params.moviePk)
  },
  beforeUnmount() {
    this.movie.genres.forEach(id => {
      this.profile.genre_score_set.forEach(object => {
          if (object.genre === id) {
            object.score += this.rating
          }
        })
    });
    this.$store.dispatch('scoreUpdate', this.profile)
  },
  watch: {
    username: function () {
      this.fetchProfile(this.username)
    }
  }
}
</script>

<style>


</style>
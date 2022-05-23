<template>
  <div>
  <div class="text-center">
    <v-rating
      v-model="score_set.score"
      icon-label="custom icon label text {0} of {1}"
      @input="onClick"
    ></v-rating>
    {{ this.movie.title }}
    <!-- 별값을 고정 해야 함. -->
    <!--  -->


  </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieDetail',
  data() {
    return {
      score_set: {
        user: '',
        movie: this.$route.params.moviePk,
        score: 0
    },
  }},
  props: {
    username: String,
  },
  computed: {
    ...mapGetters(['movie', 'currentUser', 'profile']),
    
  },
  methods: {
    ...mapActions(['getMovie', 'scoreUpdate', 'fetchProfile', 'fetchCurrentUser']),
    onClick() {
      this.movie.genres.forEach(id => {
        this.profile.genre_score_set.forEach(object => {
            if (object.genre === id) {
              object.score += this.score
            }
          })
      });
      this.score_set.user = this.currentUser.pk
      this.profile = {...this.profile, ...this.score_set}
      this.$store.dispatch('scoreUpdate', this.profile)
    },
  },
  created() {
    this.getMovie(this.$route.params.moviePk)
  },
  watch: {
    username: function () {
      this.fetchProfile(this.username)
    },
  }
}
</script>

<style>


</style>
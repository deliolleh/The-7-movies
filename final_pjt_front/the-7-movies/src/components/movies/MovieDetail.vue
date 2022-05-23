<template>
  <div>
  <div class="text-center">
    <v-rating
      v-if="!score_set.score"
      v-model="score_set.score"
      :value="this.profile.score_set.score"
      icon-label="custom icon label text {0} of {1}"
      @input="onClick"
    ></v-rating>
      <v-rating
      v-else
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
      pro() {
        return this.username
      }
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
      console.log(this.profile.genre_score_set);
      this.movie.genres.forEach(id => {
        this.profile.genre_score_set.forEach(object => {
            if (object.genre === id) {
              object.score += this.score_set.score
              console.log(this.score_set.score, object.score);
            }
          })
      });
      console.log(this.profile.genre_score_set);
      this.score_set.user = this.currentUser.pk
      console.log(this.score_set);
      this.profile.score_set = this.score_set
      console.log('이건 별 매길때');
      console.log(this.profile);
      console.log('별매긴 후');
      const payload = {
        profile: this.profile,
        moviePk: this.$route.params.moviePk
      }
      this.$store.dispatch('scoreUpdate', payload)
    },
    checkReview() {
      console.log(this.$store.getters, 'profile');
      this.profile.score_set.forEach(object => {
        if (object.movie === this.$route.params.moviePk ) {
          this.score = object.score
          console.log('체크리뷰');
        } 
      });
    }
  },
  created() {
    this.getMovie(this.$route.params.moviePk)
    },
  watch: {
    username: function () {
      this.fetchProfile(this.username)
    },
    curr: function () {
      this.checkReview()
    },
    pro() {
    }
  },
}
</script>

<style>


</style>
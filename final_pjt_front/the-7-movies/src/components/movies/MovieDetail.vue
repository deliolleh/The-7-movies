<template>
  <v-app>
    <v-container>
      <v-scroll-x-transition mode="in" hide-on-leave="true">
        <v-row
        justify="center"
        >
          <v-card
          max-width="400"
          >
            <v-img
              :src="movie.poster_path"
            >
            </v-img>
          </v-card>
          <v-card
          width="400"
          color="#FAFAFAFF"
          >
            <v-card-title>
              {{ movie.title }}                 
              
            </v-card-title>
            <v-card-text>
              감독 : {{ movie.director }}
              <br>
              개봉 : {{ movie.release_date }}
              <br>
              개요 : {{ movie.genres[0].name }} | 평점 : {{ average }}
              <hr>
              <br>
              {{ movie.overview }}
              <v-spacer></v-spacer>
              <router-link :to="{name:'create'}">
                리뷰 쓰러 가기
              </router-link>

            </v-card-text>
          </v-card>
        </v-row>
      </v-scroll-x-transition>

    <div class="text-center">
      <!-- <v-rating
        v-model="score_set.score"
        icon-label="custom icon label text {0} of {1}"
        @input="onClick"
        background-color="orange lighten-3"
        color="orange"
        large
      ></v-rating> -->
        <v-rating
        v-model="score_set.score"
        icon-label="custom icon label text {0} of {1}"
        @input="onClick"
        background-color="orange lighten-3"
        color="orange"
        large
      ></v-rating>
    </div>
  </v-container>
  </v-app>
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
    average() {
      const avg = this.movie.vote_score/this.movie.vote_count
      return avg
    }
    
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
  },
}
</script>

<style>

div.v-card {
  background-color: rgba(233, 245, 233, 1);
}

</style>
<template>
<div>
    <v-container class="mt-10">
        <v-row>
            <v-col cols="12" sm="4">
              <v-hover
                v-slot="{ hover }"
                open-delay="200"
              >
                <v-card :elevation="hover ? 16 : 2"
                  :class="{ 'on-hover': hover }">
                    <router-link :to="{name: 'reviewcreate', params:{movieTitle: movie.title} }">
                          <v-img :src="movie.poster_path" alt="" class=""/>
                    </router-link> 
                </v-card>
              </v-hover>
            </v-col>  
            <v-col cols="12" sm="8">
                <h1 class="grey--text text-darken-3 mt-5">{{this.movie.title}}</h1>
                <p>감독 : {{ movie.director }}</p>
                  <div class="subtitle-2 grey--text">
                    <p>개봉 : {{movie.release_date}}</p>
                    <p> 평점 : {{ movie.vote_score }}</p>
                    <span v-for="(item, index) in movie.genres" :key="index" class="ml-1">
                          {{item.name}}
                          <span v-if="(movie.genres.length - 1 != index)">,</span>
                          </span> 
                  </div>
                <p class="mt-5 grey--text text--darken-3 subheader">{{this.movie.overview}}</p>
          <div class="subtitle-2 grey--text ml-5">
            <span> 영화 평점 남기기 </span>
            <v-icon>mdi-arrow-down</v-icon>
            <v-btn class="mx-5 grey--text" @click="onReset">reset</v-btn>
          </div>
          <v-rating
          v-model="score_set.score"
          icon-label="custom icon label text {0} of {1}"
          @input="onClick"
          background-color="orange lighten-3"
          color="orange"
          large
        >
        </v-rating>
        <router-link :to="{ name: 'reviewcreate', params:{movieTitle: movie.title} }">
          <v-btn 
            color="primary"
            style="width: 250px"
          >리뷰 작성 </v-btn>
        </router-link>
          <best-review></best-review>
            </v-col>
        </v-row> 
        <!-- <v-divider class="mt-2"></v-divider>
         <Cast :casts="movie.credits.cast"/>
         <v-divider class="mt-2"></v-divider>
         <Images :images="movie.images.backdrops" /> -->
    </v-container>
 
    
  </div>
  

</template>

<script>
// import Cast from "../components/Cast.vue"
// import Images from "../components/Images.vue"
import BestReview from '@/components/movies/BestReview'
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieDetail',
  data() {
    return {
      videoURL: '',
      score_set: {
        user: '',
        movie: this.$route.params.moviePk,
        score: 0
    },
  }},
  components: {
    BestReview,
  },
  computed: {
    ...mapGetters(['movie', 'currentUser', 'profile', 'currentMovie']),
    
  },
  methods: {
    ...mapActions(['getMovie', 'scoreUpdate', 'fetchProfile',
    'fetchCurrentUser', 'getMoviePk', 'resetScore']),
    onClick() {
      console.log(this.profile.genre_score_set);
      this.movie.genres.forEach(genre => {
        this.profile.genre_score_set.forEach(object => {
            if (object.genre === genre.id) {
              console.log('출력');
              object.score += this.score_set.score
              console.log(this.score_set.score, object.score);
            }
          })
      });
      this.score_set.user = this.currentUser.pk
      this.profile.score_set = this.score_set
      const payload = {
        profile: this.profile,
        moviePk: this.$route.params.moviePk
      }
      this.$store.dispatch('scoreUpdate', payload)
    },
    checkReview() {
      this.profile.score_set.forEach(object => {
        if (object.movie === Number(this.$route.params.moviePk) ) {
          this.score_set.score = object.score
        }
      });
    },
    onReset() {
      this.movie.genres.forEach(genre => {
        this.profile.genre_score_set.forEach(object => {
            if (object.genre === genre.id) {
              object.score -= this.score_set.score
              console.log('되나?');
            }
          })
      });
      this.score_set.score = 0
      this.score_set.user = this.currentUser.pk
      this.profile.score_set = this.score_set
      const payload = {
        profile: this.profile,
        moviePk: this.$route.params.moviePk
      }
      this.$store.dispatch('resetScore', payload)
    }
  },
  created() {
    this.getMovie(this.$route.params.moviePk)
    this.checkReview()
    this.getMoviePk(this.$route.params.moviePk)
  },
}
</script>

<style scoped>

</style>
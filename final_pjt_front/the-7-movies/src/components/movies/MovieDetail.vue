<template>
<div>
    <v-container>
        <v-row>
            <v-col cols="12" sm="4">
                <v-hover
        v-slot="{ hover }"
        open-delay="200"
      >
<v-card :elevation="hover ? 16 : 2"
          :class="{ 'on-hover': hover }">
     <router-link :to="{name: 'create'}">
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
                          <p> 평점 : {{ average }}</p>
                          <span v-for="(item, index) in movie.genres" :key="index" class="ml-1">
                                {{item.name}}
                                <span v-if="(movie.genres.length - 1 != index)">,</span>
                                </span> 
                        </div>
                <p class="mt-5 grey--text text--darken-3 subheader">{{this.movie.overview}}</p>
                <!-- <div class="mt-5">
                    <h2 class="mt-5 grey--text text--darken-3">Featured Cast</h2>
                    <div :key="index" v-for="(crew, index) in movie.credits.crew" class="mt-5">
                        <div v-if="index < 2" class="">
                            <h3>{{crew.name}}</h3>
                            <span class="grey--text">{{crew.job}}</span>
                        </div>
                    </div>
                </div> -->
                <!-- <v-dialog
                v-model="dialog"
                persistent
                max-width="800px"
                >
                    <template v-slot:activator="{on, attrs}">
                        <v-btn tile color="error" v-bind="attrs" v-on="on" @click.prevent="openYouTubeModel">
                            <v-icon left>mdi-play</v-icon>Play
                        </v-btn>
                    </template>
                    <v-card>
                        <v-card-title>
                            <span class="headline">{{this.movie.title}}</span>
                        </v-card-title>
                        <v-card-text>
                            <v-container>
                                <v-row>
                                    <v-col cols="12" sm="">
                                        <div class="iframe-container">
                                            <img :src="mediaURL" v-if="!isVideo" />
                                            <iframe allowfullscreen v-if="isVideo" :src="mediaURL"></iframe>
                                        </div>
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="error" text @click="dialog = flase">Close</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog> -->
          <div class="subtitle-2 grey--text ml-5">
            <span> 영화 평점 남기기 </span>
            <v-icon>mdi-arrow-down</v-icon>
          </div>
                <v-rating
          v-model="score_set.score"
          icon-label="custom icon label text {0} of {1}"
          @input="onClick"
          background-color="orange lighten-3"
          color="orange"
          large
        ></v-rating>
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
    }
  },
  created() {
    this.getMovie(this.$route.params.moviePk)
    this.checkReview()
  },
}
</script>

<style>
.iframe-container {
  overflow: hidden;
  padding-top: 56.25%;
  position: relative;
}
.iframe-container iframe {
   border: 0;
   height: 100%;
   left: 0;
   position: absolute;
   top: 0;
   width: 100%;
}
</style>
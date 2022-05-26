<template>
  <v-app>
    <h2 class="mx-3 grey--text text-center mt-10">
      선호 하는 영화를 선택해주세요
    </h2>
      <!-- 2장씩 받아야함. -->
      <br>
      <v-container>
        <v-progress-linear
          color="primary"
          height="50"
          :value="progress"
          striped
        ></v-progress-linear>
      </v-container>
      <section id="recommends">
        <v-row id="cards"
          class="ma-2"
          justify="center"
          v-if="index < 16"
        >
        <v-hover
        >
          <v-card 
            id="left"
            max-width="350"
            @click="bigin_left()"
            class=" flex d-flex flex-column"
            >
          <v-expand-x-transition>
            <v-img
              :src="this.recommend[this.index].poster_path"
              :key="index"
            >
            </v-img>
          </v-expand-x-transition>
            <v-card-title class="subtitle-2">{{recommend[this.index].title}}</v-card-title>
            <v-card-text>
              <v-row align="center" class="mx-0">
                  <v-rating :value="recommend[this.index].vote_score / 2" color="amber" dense half-increments readonly size="14">
                  </v-rating>
                  <div class="grey--text ml-4">
                      {{recommend[this.index].release_date}}
                  </div>
              </v-row>
            </v-card-text>
          </v-card>
        </v-hover>
        <v-hover>
          <v-card id="right"
            max-width="350"
            @click="bigin_right()"
            class=" flex d-flex flex-column"
            >
            <!-- <v-scroll-x-transition> -->
        <v-expand-x-transition>
            <v-img
              :src="this.recommend[this.index+1].poster_path"
              :key="index+1"
            >
            </v-img>
        </v-expand-x-transition>
                      <v-card-title class="subtitle-2">{{recommend[this.index+1].title}}</v-card-title>
            <v-card-text>
              <v-row align="center" class="mx-0">
                  <v-rating :value="recommend[this.index+1].vote_score / 2" color="amber" dense half-increments readonly size="14">
                  </v-rating>
                  <div class="grey--text ml-4">
                      {{recommend[this.index+1].release_date}}
                  </div>
              </v-row>
            </v-card-text>
          </v-card>
        </v-hover>
        </v-row>
      </section>
  </v-app>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
// import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'RecommendView',
  data() {
    return {
      index: 0,
      username: this.$route.params.username,
      ...this.profile
    }
  },
  methods: {
    ...mapActions(['getRecommend', 'fetchProfile']),
     goNext(idx) {
      const left = document.querySelector('#left > img')
      const right = document.querySelector('#right > img')
      left.setAttribute('src', this.recommend[idx].poster_path)
      right.setAttribute('src', this.recommend[idx+1].poster_path)
    },
    bigin_left() {
      this.recommend[this.index].genres.forEach(genre => {
        this.profile.genre_score_set.forEach(object => {
          if (object.genre === genre.id) {
            object.score += 1
          }
        })
      });
      this.index = this.index + 2
      // if (this.index < this.recommend.length-1) {
      //   return this.goNext(this.index)
      // } else {
      //   console.log('일로오나?');
      //   console.log(this.profile);
      //   this.$store.dispatch('scoreCreate', this.profile)
      //   this.$router.push({name: 'recommend'})
      //   console.log('routing??');
      //   return
      // }
    },
    bigin_right() {
      this.recommend[this.index+1].genres.forEach(genre => {
        this.profile.genre_score_set.forEach(object => {
          if (object.genre === genre.id) {
            object.score += 1
          }
        })
      });
      this.index = this.index + 2
      //  if (this.index < this.recommend.length-1) {
      //   return this.goNext(this.index)
      // } else {
      //   console.log('오른쪽?');
      //   console.log(this.profile);
      //   this.$store.dispatch('scoreCreate', this.profile)
      //   this.$router.push({name: 'recommend'})
      //   return
      // }
    },
  },
  computed: {
    ...mapGetters(['profile', 'recommend']),
    progress() {
      return this.index * 7.5
    }
  },
  watch: {
    index() {
      if (this.index===16) {
        this.$store.dispatch('scoreCreate', this.profile)
          .then(() => this.$router.push({name: 'recommend'}))
      }
    }
  },
  created() {
    this.getRecommend()
    this.fetchProfile(this.username)
  },
}
</script>

<style scoped>

/* img {
  -webkit-transition: all 3s ease;
  transition: all 3s ease;
} */


#left {
  margin: 15px;
}

#right {
  margin: 15px;
}

/* .slide-fade-enter-active {
  opacity: 1;
  z-index: 10;
}

.slide-fade-leave-active {
  opacity: 1;
}

.slide-fade-enter,
.slide-fade-leave-to {
  opacity: 0;
} */

</style>
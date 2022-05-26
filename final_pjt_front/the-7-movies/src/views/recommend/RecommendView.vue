<template>
  <v-app>
      <h1> 선호 하는 영화를 선택해주세요 </h1>
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
        >
          <v-card id="left"
            max-width="350"
            @click="bigin_left()"
            class=" flex d-flex flex-column"
            >
<<<<<<< HEAD
          <!-- <v-scroll-x-transition> -->
          <v-fade-transition>
              <img
                :src="this.recommend[this.index].poster_path"
                :key="this.recommend[this.index].poster_path"
              >
          </v-fade-transition>
          <!-- </v-scroll-x-transition> -->
=======
          <v-expand-x-transition>
            <v-img
              :src="this.recommend[this.index].poster_path"
              :key="this.recommend[this.index].poster_path"
            >
            </v-img>
          </v-expand-x-transition>
>>>>>>> f2f730665ac7307e08ac02d4573a01782b81b362
          </v-card>
          <v-card id="right"
            max-width="350"
            @click="bigin_right()"
            class=" flex d-flex flex-column"
            >
            <!-- <v-scroll-x-transition> -->
        <v-expand-x-transition>
            <v-img
              :src="this.recommend[this.index+1].poster_path"
              :key="this.recommend[this.index+1].poster_path"
            >
            </v-img>
            <!-- </v-scroll-x-transition> -->
            <!-- <router-link :to="{name: 'movies', params: `${this.recommend[this.index+1].}`}">
            </router-link> -->
<<<<<<< HEAD
        </v-fade-transition>
=======
        </v-expand-x-transition>
>>>>>>> f2f730665ac7307e08ac02d4573a01782b81b362
          </v-card>
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
      this.recommend[this.index].genres.forEach(id => {
        this.profile.genre_score_set.forEach(object => {
          if (object.genre === id) {
            object.score += 1
          }
        })
      });
      this.index = this.index + 2
      if (this.index < this.recommend.length-1) {
        return this.goNext(this.index)
      } else {
        console.log('일로오나?');
        console.log(this.profile);
        this.$store.dispatch('scoreCreate', this.profile)
        this.$router.push({name: 'recommend'})
        console.log('routing??');
        return
      }
    },
    bigin_right() {
      this.recommend[this.index+1].genres.forEach(id => {
        this.profile.genre_score_set.forEach(object => {
          if (object.genre === id) {
            object.score += 1
          }
        })
      });
      this.index = this.index + 2
       if (this.index < this.recommend.length-1) {
        return this.goNext(this.index)
      } else {
        console.log('오른쪽?');
        console.log(this.profile);
        this.$store.dispatch('scoreCreate', this.profile)
        this.$router.push({name: 'recommend'})
        return
      }
    },
  },
  computed: {
    ...mapGetters(['profile', 'recommend']),
    progress() {
      return this.index * 7.5
    }
  },
  created() {
    this.getRecommend()
    this.fetchProfile(this.username)
  }
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

.slide-fade-enter-active {
  transition: all 2s ease;
}
.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
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
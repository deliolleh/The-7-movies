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
          <v-scroll-x-transition mode="in" hide-on-leave="true">
            <img
              :src="this.recommend[this.index].poster_path"
              :key="this.recommend[this.index].poster_path"
            >
          </v-scroll-x-transition>
          </v-card>
          <v-card id="right"
            max-width="350"
            @click="bigin_right()"
            class=" flex d-flex flex-column"
            >
            <v-scroll-x-transition mode="in" hide-on-leave="true">
            <img
              :src="this.recommend[this.index+1].poster_path"
              :key="this.recommend[this.index+1].poster_path"
            >
            </v-scroll-x-transition>
            <!-- <router-link :to="{name: 'movies', params: `${this.recommend[this.index+1].}`}">
            </router-link> -->
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
      if (this.index < this.recommend.length) {
        return this.goNext(this.index)
      } else {
        const left = document.querySelector('#left > img')
        const right = document.querySelector('#right > img')
        left.removeAttribute('src')
        right.removeAttribute('src')
        return  this.$store.dispatch('scoreUpdate', this.profile)
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
            if (this.index < this.recommend.length) {
        return this.goNext(this.index)
      } else {
        const left = document.querySelector('#left > img')
        const right = document.querySelector('#right > img')
        left.removeAttribute('src')
        right.removeAttribute('src')
        console.log(this.profile);
        return  this.$store.dispatch('scoreUpdate', this.profile)
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

img {
  -webkit-transition: all 3s ease;
  transition: all 3s ease;
}


#left {
  margin: 15px;
}

#right {
  margin: 15px;
}

.slide-fade-enter-active {
  opacity: 1;
  z-index: 10;
}

.slide-fade-leave-active {
  opacity: 1;
}

.slide-fade-enter,
.slide-fade-leave-to {
  opacity: 0;
}

</style>
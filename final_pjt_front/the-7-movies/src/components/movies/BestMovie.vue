<template>
  
  <vueper-slides fade :touchable="false" 
    fixed-height="1000px"
    autoplay
    >
    <vueper-slide
      v-for="(movie, idx) in bestmovie"
      :key="idx"
      :image="movie.backdrop_path"
      >
      <!-- 로그인 했을 경우 -> 영화 정보 -->
      <template 
      #content>
        <div
        v-if="isLoggedIn"
        id="homelogin"
        >
      <h1>
      <i class="fa-solid fa-video"></i> Best Movies
      </h1>
        <p style="color:white">
         {{ idx+1 }}. {{ movie.title }}
        </p>
          <router-link :to="{name: 'movieDetail' , params: {moviePk: movie.pk} }">
            <v-btn
            color="primary"
            class="pa-6 font-weight-bold mr-4"
            style="width : 300px"
            >영화 상세 정보</v-btn>
            </router-link>
            <br>
        </div>
        <div v-else-if="!isLoggedIn" id="homeguest">
          <p class="guestText"> 로그인 하고, <br> 취향에 맞는 영화 찾기! </p>
          <router-link :to="{name: 'login'}">
            <v-btn
              color="primary"
              class="pa-6 my-3 font-weight-bold mr-4"
              block
            >Sign in</v-btn>
          </router-link>
          <router-link :to="{name: 'signup'}">
            <v-btn
            color="primary"
            class="pa-6 font-weight-bold mr-4"
            block
            >Sign up</v-btn>
          </router-link>
        </div>
      </template>
      <!-- 로그인 하지 않았을 경우 -> 로그인  -->
    </vueper-slide>
  </vueper-slides>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'


export default {
  name: 'BestMovie',
  components: { VueperSlides, VueperSlide },
  computed: {
    ...mapGetters(['bestmovie', 'isLoggedIn'])
  },
  methods: {
    ...mapActions(['getBestMovie'])
  },
  created() {
    this.getBestMovie()
  },
}
</script>

<style scoped>

#homelogin {
  color: whitesmoke;
  font-size: 3em;
  margin-bottom: 0.5em;
  position: absolute;
  left: 50px;
  bottom: 180px;
}

#homeguest {
  color: whitesmoke;
  font-size: 3em;
  margin-bottom: 0.5em;
  position: absolute;
  left: 50px;
  bottom: 180px;
}

div.vueperslide__title {
  color: whitesmoke;
  font-size: 5em;
  margin-bottom: 0.5em;
  opacity: 0.7;
  position: absolute;
  left: 0px;
}

div.vueperslide__content {
  color: whitesmoke;
  font-size: 3em;
  margin-bottom: 0.5em;
  opacity: 0.7;
  position: absolute;
  left: 0px;
}



</style>


<template>
  <div>
    <h1 class="mx-3 text-center mt-10">
      The 7 Movies for You
    </h1>
    <carousel-3d
      :controls-visible="true"
      :clickable="false"
      :key="recommends.length"
      :listData="recommends"
      :height="500"
    >
      <slide :index="i" :key="i" v-for="(movie, i) in recommends">
        <figure>
          <img :src="movie.poster_path" />
          <figcaption>
            <v-btn :to="`/movies/${movie.pk}`" text color="white"> {{ movie.title }}</v-btn>
          </figcaption>
        </figure>
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
import { Carousel3d, Slide } from "vue-carousel-3d";
import { mapGetters, mapActions } from 'vuex';

export default {
  components: {
    Carousel3d,
    Slide,
  },
  computed: {
    ...mapGetters(['recommends'])
  },
  methods: {
    ...mapActions(['getRecommends']),
    // async fetchRecommends() {
      //   const response = await this.getRecommends
    //   this.recommends = response.data.results
    //   console.log(this.upcomingMovies);
    // },
  },
  created() {
    // bus.$emit('start:spinner')
    // setTimeout(() => {
    //   this.getRecommends()
    //     .then(() => {
    //       console.log('영화받아옴');
    //       bus.$emit('end:spinner')
    //     })
    // }, 3000)
    },
};
</script>

<style scoped>

.carousel-3d-container figure {
  margin: 0;
}
.carousel-3d-container figcaption {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  bottom: 0;
  position: absolute;
  bottom: 0;
  padding: 15px;
  font-size: 12px;
  min-width: 100%;
  box-sizing: border-box;
}

.next span,
.prev span {
  color: red;
}
</style>
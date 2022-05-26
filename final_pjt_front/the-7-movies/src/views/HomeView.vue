<template>
  <v-app height="100%">
    <section height="100%">
      <best-movie></best-movie>
    </section>
      <section>
        <recommend-movie v-if="this.isLoggedIn"></recommend-movie>
      </section>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'
import BestMovie from '@/components/movies/BestMovie'
import RecommendMovie from '@/components/movies/RecommendMovie'
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    BestMovie,
    RecommendMovie,
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  mounted () {
  window.scrollTo(0, 0)
  }
}
</script>

<style scoped>

#wrapper {
  position: relative;
}

#homelogin {
  width: 500px;
  position: absolute;
  font-size: 100px;
}


</style>
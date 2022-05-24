<template>
  <v-app>
    <section>
      <best-movie></best-movie>
    </section>
    <section>
      <weekly-best v-if="!this.isLoggedIn"></weekly-best>
      <recommend-movie v-else></recommend-movie>
    </section>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'
import BestMovie from '@/components/movies/BestMovie'
import WeeklyBest from '@/components/movies/WeeklyBest'
import RecommendMovie from '@/components/movies/RecommendMovie'
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
    BestMovie,
    WeeklyBest,
    RecommendMovie,
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  }
}
</script>

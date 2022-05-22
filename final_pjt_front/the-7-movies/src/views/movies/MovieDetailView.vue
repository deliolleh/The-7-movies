<template>
  <div>
    <section>
      <movie-detail
        :username="this.currentUser.username"
      ></movie-detail>
    </section>
    <section>
      <best-review></best-review>
    </section>
  </div>
</template>

<script>
import MovieDetail from '@/components/movies/MovieDetail'
import BestReview from '@/components/movies/BestReview'
import { mapGetters } from 'vuex'

export default {
  name: 'MovieDetailView',
  components: {
    MovieDetail,
    BestReview,
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  created() {
    this.$store.dispatch('fetchCurrentUser')
  }
}
</script>

<style>

</style>
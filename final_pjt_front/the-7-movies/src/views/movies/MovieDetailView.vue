<template>
  <div class="d-flex flex-column">
    <section>
      <movie-detail
        :username="this.currentUser.username"
      ></movie-detail>
    </section>
  </div>
</template>

<script>
import MovieDetail from '@/components/movies/MovieDetail'
import { mapGetters } from 'vuex'

export default {
  name: 'MovieDetailView',
  components: {
    MovieDetail,
  },
  computed: {
    ...mapGetters(['currentUser', 'profile']),
  },
  created() {
  }
}
</script>

<style>

</style>
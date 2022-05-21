<template>
  <div>
    <section>
      <movie-detail
       :moviePk="moviePk"
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

export default {
  name: 'MovieDetailView',
  data() {
    return {
      moviePk: this.$route.params.moviePk
    }
  },
  components: {
    MovieDetail,
    BestReview,
  }
}
</script>

<style>

</style>
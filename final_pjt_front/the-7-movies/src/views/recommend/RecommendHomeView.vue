<template>
  <section class="my-5">
    <recommend-movie></recommend-movie>
    <the-spinner :loading="this.loadingStatus"></the-spinner>
  </section>

</template>

<script>
import RecommendMovie from '@/components/movies/RecommendMovie'
import TheSpinner from '@/components/common/TheSpinner'
import bus from '@/utils/bus'
export default {
  name: 'RecommendHomeView',
  data() {
  return {
    loadingStatus: false
    }
  },
  components : {
    RecommendMovie,
    TheSpinner
  },
  created() {
    bus.$on('start:spinner', this.startSpinner)
    bus.$on('end:spinner', this.endSpinner)
    this.fetchCurrentUser()
  },
  beforeDestroy() {
    bus.$off('start:spinner', this.startSpinner)
    bus.$off('end:spinner', this.endSpinner)
  }
}
</script>

<style>

</style>
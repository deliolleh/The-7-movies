<template>
  <section class="my-5">
    <recommend-movie></recommend-movie>
  </section>

</template>

<script>
import RecommendMovie from '@/components/movies/RecommendMovie'
import { mapActions } from 'vuex'
import bus from '@/utils/bus'

export default {
  name: 'RecommendHomeView',
  components : {
    RecommendMovie,
  },
  methods: {
    ...mapActions(['fetchCurrentUser'])
  },
  created() {
    this.fetchCurrentUser()
  },
  mounted() {
    bus.$emit('end:spinner')
  }
}
</script>

<style>

</style>
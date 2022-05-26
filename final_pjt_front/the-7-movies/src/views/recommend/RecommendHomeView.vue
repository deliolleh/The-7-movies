<template>
  <section class="my-5">
    <recommend-movie></recommend-movie>
    <router-link :to="{name: 'algorecommend', params: {username:currentUser.username}}">
      <h2 class="grey--text text-center mt-5"> 다시 추천 받기</h2>
    </router-link>

  </section>

</template>

<script>
import RecommendMovie from '@/components/movies/RecommendMovie'
import bus from '@/utils/bus'
import { mapGetters } from 'vuex'

export default {
  name: 'RecommendHomeView',
  components : {
    RecommendMovie,
  },
  computed: {
    ...mapGetters(['currentUser'])
  },
  mounted() {
    bus.$emit('end:spinner')
  }
}
</script>

<style scoped>

a {
  text-decoration: none;
}

</style>
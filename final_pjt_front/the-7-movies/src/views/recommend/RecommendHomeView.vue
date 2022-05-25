<template>
  <section class="my-5">
    <recommend-movie></recommend-movie>
    <div>
      {{}}
    </div>
  </section>

</template>

<script>
import RecommendMovie from '@/components/movies/RecommendMovie'

export default {
  name: 'RecommendHomeView',
  components : {
    RecommendMovie,
  }
}
</script>

<style>

</style>
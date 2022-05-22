<template>
  <div> 
    이것은 로그인 되었을 때 보여지는 화면
    <v-card
      v-for="(recommend,idx) in recommends"
      :key="idx"
    >
    <img :src="recommend.poster_path" alt="">
    </v-card>
    </div>
  
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'RecommendMovie',
  computed: {
    ...mapGetters(['recommends'])
  },
  methods: {
    ...mapActions(['getRecommends'])
  },
  created() {
    this.getRecommends()
  }
}
</script>

<style>

</style>
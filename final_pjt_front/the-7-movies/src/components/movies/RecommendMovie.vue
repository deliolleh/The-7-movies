<template>

<!-- 수정 필요 -->
<vueper-slides
  class="no-shadow"
  :visible-slides="3"
  :slide-ratio="1 / 4"
  :dragging-distance="70"
  >
  <template #arrow-left>
    <i class="icon icon-arrow-left" />
  </template>

  <template #arrow-right>
    <i class="icon icon-arrow-right" />
  </template>
  <vueper-slide v-for="(recommend,idx) in recommends"
      :key="idx"
      :image="recommend.poster_path"
       />
</vueper-slides>

    <!-- <vueper-slides
    class="no-shadow"
    :visible-slides="3"
    :slide-ratio="1 / 4"
    :dragging-distance="70">
    <vueper-slide v-for="(recommend,idx) in recommends"
      :key="idx"
      :image="recommend.poster_path"
       />
    </vueper-slides> -->
    <!-- <v-card
      v-for="(recommend,idx) in recommends"
      :key="idx"
    >
    <img :src="recommend.poster_path" alt="">
    </v-card>
   -->
</template>

<script>
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'RecommendMovie',
  components: { VueperSlides, VueperSlide },
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
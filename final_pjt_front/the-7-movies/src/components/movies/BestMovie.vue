<template>
  <vueper-slides fade :touchable="false" 
    fixed-height="1000px"
    >
    <vueper-slide
      v-for="(slide, i) in bestmovie"
      :key="i"
      :image="slide.backdrop_path"
      :title="slide.title"
      :content="slide.content" />
</vueper-slides>

      <!-- <v-carousel-item
        v-for="(item,i) in bestmovie"
        :key="i"
        width="100%"
      >
      </v-carousel-item> -->
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'


export default {
  name: 'BestMovie',
  components: { VueperSlides, VueperSlide },
  computed: {
    ...mapGetters(['bestmovie'])
  },
  methods: {
    ...mapActions(['getBestMovie'])
  },
  created() {
    this.getBestMovie()
  },
  slides: [
  {
    title: 'El Teide Volcano, Spain',
    content: 'Photo by Max Rive',
    // You can also provide a URL for the image.
  },
  // Other slides.
]
}
</script>

<style>

</style>
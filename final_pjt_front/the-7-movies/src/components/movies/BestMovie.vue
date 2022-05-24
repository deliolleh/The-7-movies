<template>
  <vueper-slides fade :touchable="false" autoplay>
  <vueper-slide
    v-for="(slide, i) in bestmovie"
    :key="i"
    :image="slide.poster_path"
    :title="slide.title"
    :content="slide.content" />
</vueper-slides>

      <!-- <v-carousel-item
        v-for="(item,i) in bestmovie"
        :key="i"
        :src="item.poster_path"
        width="1000"
        height="auto"
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
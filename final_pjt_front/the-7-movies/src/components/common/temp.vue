<template>
  <!-- <v-app>
    <v-sheet
    class="mx-auto"
    elevation="8"
    max-width="800"
  >
    <v-slide-group
      v-model="model"
      class="pa-4"
      show-arrows
    >
      <v-slide-item
        v-for="n in 15"
        :key="n"
        v-slot="{ active, toggle }"
      >
        <v-card
          :color="active ? 'primary' : 'grey lighten-1'"
          class="ma-4"
          height="200"
          width="100"
          @click="toggle"
        >
          <v-row
            class="fill-height"
            align="center"
            justify="center"
          >
            <v-scale-transition>
              <v-icon
                v-if="active"
                color="white"
                size="48"
                v-text="'mdi-close-circle-outline'"
              ></v-icon>
            </v-scale-transition>
          </v-row>
        </v-card>
      </v-slide-item>
    </v-slide-group>

    <v-expand-transition>
      <v-sheet
        v-if="model != null"
        height="200"
        tile
      >
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <h3 class="text-h6">
            Selected {{ model }}
          </h3>
        </v-row>
      </v-sheet>
    </v-expand-transition>
  </v-sheet> -->
  
  <!-- <v-app>
      <v-row
        dense
        justify="center">
        <v-col
          v-for="(recommend,idx) in recommends"
          cols= "3"
          :key="idx"
          height=300
          >
          <v-card
            height="100%"
            >
            <router-link
              :to="{ name: 'movieDetail', params:{ moviePk: recommend.pk} }">
              <v-img
                :src="recommend.poster_path"
                height="100%"
                ></v-img>
            </router-link>
          </v-card>
        </v-col>
      </v-row>
  </v-app>
  </v-app> -->
  

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
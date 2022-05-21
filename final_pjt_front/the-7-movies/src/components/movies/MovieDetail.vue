<template>
  <div>
    <v-row>
      <v-card>
        <v-img
          :src="movie.poster_path">
        </v-img>
      </v-card>
      <v-card>
        <v-row
          align="center"
          class="mx-0"
        >
          <v-rating
            :value="4.5"
            color="amber"
            dense
            half-increments
            readonly
            size="14"
          ></v-rating>

          <div class="grey--text ms-4">
            4.5 (413)
          </div>
        </v-row>

        <div class="my-4 text-subtitle-1">
          {{ movie.title }}
        </div>

        <div>{{ movie.overview }}</div>
      </v-card>
    </v-row>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'MovieDetail',
  props: {
    moviePk: String,
  },
  computed: {
    ...mapGetters(['movie'])
  },
  methods: {
    ...mapActions(['getMovie'])
  },
  created() {
    this.getMovie(this.moviePk)
  }
}
</script>

<style>
img {
  width: 500px;
}

</style>
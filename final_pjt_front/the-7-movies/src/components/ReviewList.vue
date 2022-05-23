<template>
  <div id="ReviewTable">
      <v-row>
        <v-col
          cols="10"
          offset="2"
        >
          <div id="main">
              <v-btn
              elevation="2"
              color="success"
              class="mr-4"
              >
                <router-link style="color: white; text-decoration: none;" :to="{name: 'create'}">review 생성</router-link>
              </v-btn>
          </div>
        </v-col>
      </v-row>
    <review-list-item
    v-for="(item, idx) in reviews" :key="idx" :item="item"
    ></review-list-item>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
  },
  computed: {
    ...mapGetters(['reviews'])
  },
  methods: {
    ...mapActions(['fetchReviews'])
  },
  created() {
    this.fetchReviews()
  }
}
</script>

<style>
  div {
    margin: 8px 0;
  }
  
</style>
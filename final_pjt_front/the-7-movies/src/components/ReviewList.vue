<template>
  <div>
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
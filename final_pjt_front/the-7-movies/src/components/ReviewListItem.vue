<template>
  <div>
    <div
      :v-for="(review, idx) in reviews" :key="idx"
    >
      {{ review.title }}
    </div>
    <!-- review 목록을 받아서 화면에 뿌리는 역할 -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'ReviewListItem',
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

</style>
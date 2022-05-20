<template>
  <div>
    <h1>New Review</h1>
    <review-form></review-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import ReviewForm from '@/components/ReviewForm'
export default {
  name: 'ReviewNew',
  components: {
    ReviewForm,
  },
  methods: {
    ...mapActions(['createReview'])
  }
}
</script>

<style>

</style>
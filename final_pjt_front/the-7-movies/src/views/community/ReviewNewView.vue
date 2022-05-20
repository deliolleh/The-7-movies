<template>
  <div>
    <h1>New Review</h1>
    <review-form :review="review" action="create"></review-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import ReviewForm from '@/components/ReviewForm'
export default {
  name: 'ReviewNewView',
  components: {
    ReviewForm,
  },
  data() {
    return {
      review: {
        moviePk: null,
        title: '',
        content: '',
      }
    }
  },
  methods: {
    ...mapActions(['createReview'])
  },
}
</script>

<style>

</style>
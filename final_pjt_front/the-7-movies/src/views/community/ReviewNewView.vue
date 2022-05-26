<template>
  <div>
    <review-form :review="review" action="create"></review-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import ReviewForm from '@/components/community/ReviewForm'
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
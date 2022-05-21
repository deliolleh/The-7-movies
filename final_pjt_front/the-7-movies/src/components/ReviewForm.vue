<template>
  <div>
    <search-bar></search-bar>
    <v-form 
      @submit.prevent="onSubmit"
      >
      <v-text-field
        label="제목"
        v-model="newReview.title"
      >
      </v-text-field>
      <v-textarea
          solo
          name="input-7-4"
          label="내용"
          v-model="newReview.content"
        >
        </v-textarea>
        <v-btn
      type="submit"
      color="success"
      class="mr-4"
      >
      등록
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import SearchBar from '@/components/SearchBar'
export default {
  name: 'ReviewForm',
  components: {
    SearchBar,
  },
  props: {
    review: Object,
    action: String,
  },
  data() {
    return {
      movieInput: '',
      newReview: {
        movie: 123,
        title: this.review.title,
        content: this.review.content
      }
    }
  },
  methods: {
    ...mapActions(['filteredList', 'createReview']),
     onSubmit() {
        if (this.action === 'create') {
          this.createReview(this.newReview)}
    }
  },
}
</script>

<style>

</style>
<template>
  <div>
    <v-container>
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
    </v-container>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
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
        movie: null,
        title: this.review.title,
        content: this.review.content
      }
    }
  },
  computed: {
    ...mapGetters(['currentMovie']),
  },
  methods: {
    ...mapActions(['filteredList', 'createReview', 'updateReview']),
      onSubmit() {
        if (this.action === 'create') {
          this.newReview.movie = this.currentMovie
          console.log(this.newReview);
          this.createReview(this.newReview)
        } else  {
          const payload = {
            pk: this.review.pk,
            ...this.newReview
          }
          console.log(payload);
          this.updateReview(payload)
        }
    }
  },
  watch: {
    currentMovie() {
      this.review.movie == this.$store.state.currentMovie
    }
  }
}
</script>

<style>

</style>
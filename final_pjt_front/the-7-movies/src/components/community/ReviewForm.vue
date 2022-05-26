<template>
  <v-col
    cols="4"
    class="mt-10"
  >
      <h1 style="text-align:center"> New Review </h1>
      <search-bar v-if="this.$route.name==='create'"></search-bar>
      <search-bar v-else :movietitle="this.$route.params.movieTitle"></search-bar>
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

  </v-col>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import SearchBar from '@/components/community/SearchBar'
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
        // if (this.$route.name==='create') {
          
        // }
        if (this.action === 'create') {
          this.newReview.movie = this.currentMovie
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
    },
  }
}
</script>

<style>

</style>
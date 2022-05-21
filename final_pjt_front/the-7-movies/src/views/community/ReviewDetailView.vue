<template>
  <div>
    <h1>{{ review.title }}</h1>

    <p>
      {{ review.content }}
    </p>
    
    <!-- Review Edit/Delete UI -->
    <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteReview(reviewPk)">Delete</button>
    </div>

    <!-- Review Like UI -->
    <div>
      Likeit:
      <button
        @click="likeReview(reviewPk)"
      >{{ likeCount }} ddd</button>
    </div>

    <hr />
    <!-- Comment UI -->
    <!-- <comment-list :comments="article.comments"></comment-list>  -->

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  // import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ReviewDetailView',
    // components: { CommentList },
    data() {
      return {
        reviewPk: this.$route.params.reviewPk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'review']),
      likeCount() {
        return this.review.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchReview',
        'likeReview',
        'deleteReview',
      ])
    },
    created() {
      this.fetchReview(this.reviewPk)
    },
  }
</script>

<style></style>
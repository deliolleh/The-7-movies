<template>
  <div>
    <h1>{{ review.title }}</h1>

    <p>
      {{ review.content }}
    </p>
    
    <!-- Article Edit/Delete UI -->
    <!-- <div v-if="isAuthor">
      <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteArticle(articlePk)">Delete</button>
    </div> -->

    <!-- Article Like UI -->
    <!-- <div>
      Likeit:
      <button
        @click="likeArticle(articlePk)"
      >{{ likeCount }}</button>
    </div> -->

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
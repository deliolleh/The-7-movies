<template>
  <div>
    <v-card>
      <v-system-bar>
    <!-- Review Edit/Delete UI -->
      <div v-if="isAuthor">
        <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
          <button>Edit</button>
        </router-link>
        <button @click="deleteReview(reviewPk)">Delete</button>
      </div>
      </v-system-bar>
      <v-toolbar flat>
        <v-toolbar-title> {{ review.title }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <div @click="likeReview(reviewPk)">
          <!-- Review Like UI -->
          <v-switch
            label="좋아요"
            hide-details
          ></v-switch>
        </div>
      </v-toolbar>
      <v-banner
        single-line
      >
      </v-banner>
      <v-card-text class="grey lighten-4">
        <v-sheet
          max-width="800"
          height="200"
          class="mx-auto"
        >
          {{ review.content }}
        </v-sheet>
      </v-card-text>
    </v-card>
    <div>
      <v-card>
      <!-- Comment UI -->
      <comment-list :comments="review.comments"></comment-list> 
      </v-card>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'


  export default {
    name: 'ReviewDetailView',
    components: { 
      CommentList,
     },
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
<template>
  <v-app>

  <v-container>
    <!-- <user-info></user-info> -->
    {{ review.user.username }}

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
                v-model="like"
                :input-value="like"
                label="좋아요"
                color="success"
                hide-details
              ></v-switch>
        </div>
      </v-toolbar>
      <v-banner
        single-line
      >
      </v-banner>
      <v-card-text class="grey lighten-4">
          {{ review.content }}
      </v-card-text>
    </v-card>
    <div>
      <v-card>
      <!-- Comment UI -->
      <comment-list :comments="review.comments"></comment-list> 
      </v-card>
    </div>
  </v-container>
    </v-app>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'
  // import UserInfo from '@/components/UserInfo'

  export default {
    name: 'ReviewDetailView',
    components: { 
      CommentList,
      // UserInfo,
     },
    data() {
      return {
        reviewPk: this.$route.params.reviewPk,
        like: false,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'review', 'currentUser']),
      likeCount() {
        return this.review.like_users?.length
      },
    },
    methods: {
      ...mapActions([
        'fetchReview',
        'likeReview',
        'deleteReview',
      ]),
      checkLikes() {
        this.review.like_people.forEach(object => {
          if (object.pk === this.currentUser.pk) {
            this.like = true
          }
        });
      }
    },
    created() {
      this.fetchReview(this.reviewPk)
      this.checkLikes()
    },
  }
</script>

<style></style>
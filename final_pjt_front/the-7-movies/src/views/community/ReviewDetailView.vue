<template>
  <v-app>

  <v-container>
    <!-- <user-info></user-info> -->
    <router-link :to="{ name: 'profile', params: { username: review.user.username } } ">
    <small> Reviewer : {{ review.user.username }}</small>
    </router-link>
    <v-card>
      <v-system-bar class="py-5 pl-5 ma-0">
    <!-- Review Edit/Delete UI -->
        <v-toolbar-title class="font-weight-black"> {{ review.title }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <div v-if="isAuthor">
          <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
            <button>Edit</button>
          </router-link>
          <button @click="deleteReview(reviewPk)" class="ml-1">Delete</button>
        </div>
      </v-system-bar>
      <v-toolbar flat style="margin: 0;">
        <div>{{ review.content }}</div>
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
      <!-- <v-banner
        single-line
      >
      </v-banner> -->
      <v-card-text class="grey lighten-4">
      </v-card-text>
    </v-card>
    <div>

      <comment-list-form  class="d-flex justify-end py-1"></comment-list-form>

      <!-- Comment UI -->
      <comment-list :comments="review.comments"></comment-list> 
    </div>
  </v-container>
    </v-app>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentListForm from '@/components/CommentListForm.vue'
  import CommentList from '@/components/CommentList.vue'
  // import UserInfo from '@/components/UserInfo'

  export default {
    name: 'ReviewDetailView',
    components: { 
      CommentList,
      CommentListForm,
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
      getIt () {
        return this.review
      }
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
      },
    },
    created() {
      this.fetchReview(this.reviewPk)
    },
    watch: {
      getIt() {
        this.checkLikes()
      }
    }
  }
</script>

<style scoped>

a {
  text-decoration: none;
  color: #2c3e50;
}

a:hover {
  color: #2c3e50;
  text-decoration: underline;
}
</style>
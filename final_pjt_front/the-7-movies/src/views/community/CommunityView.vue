<template>
  <div>
    <v-container>
      <v-row>
        <div id="main">
          <v-btn
          elevation="2"
          color="success"
          class="mr-4 justify-end"
          >
            <router-link style="color: white; text-decoration: none;" :to="{name: 'create'}">review 생성</router-link>
          </v-btn>
        </div>
      </v-row>
    </v-container>
    <!-- 게시글 -->
    <div>
      <review-list></review-list>
    </div>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList'

export default {
  name: 'CommunityView',
  components: {
    ReviewList,
  }
}
</script>

<style>
 #main {
   margin: 0 8px;
 }
</style>
<template>
  <div id="main">
    <v-btn
    depressed
    color="Primary">
      <router-link style="text-decoration: none;" :to="{name: 'create'}">review 생성</router-link>
    </v-btn>
    <v-divider></v-divider>
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
<template>
  <v-app>
    <!-- 게시글 -->
    <div>
      <review-list></review-list>
    </div>
  </v-app>
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
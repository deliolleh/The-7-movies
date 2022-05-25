<template>
  <v-app>
    <!-- 게시글 -->
    <div class="mt-10">
      <review-list></review-list>
    </div>
  </v-app>
</template>

<script>
import ReviewList from '@/components/ReviewList'
import bus from '@/utils/bus'

export default {
  name: 'CommunityView',
  components: {
    ReviewList,
  },
  created() {
    bus.$emit('start:spinner')
    
  }
}
</script>

<style>
 #main {
   margin: 0 8px;
 }
</style>
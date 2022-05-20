<template>
  <div>
    <div>
      <router-link :to="{name: 'create'}">review 생성</router-link>
    </div>
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

</style>
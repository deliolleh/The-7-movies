<template>
  <v-app>
    <!-- 게시글 -->
    <div>
    <h1 class="text-center mt-10">
      <i class="fa-solid fa-pen"></i> Community
    </h1>
      <review-list :currentPage="currentPage"></review-list>
    </div>
    <div class="text-center">
      <v-pagination
        v-model="currentPage"
        :length="totalPage"
        :total-visible="4"
      ></v-pagination>
    </div>
  </v-app>
</template>

<script>
import ReviewList from '@/components/community/ReviewList'
import { mapGetters } from 'vuex'

export default {
  name: 'CommunityView',
  components: {
    ReviewList,
  },
  data () {
    return {
      currentPage: 1,
    }
  },
  computed: {
    ...mapGetters(['totalPage'])
  },
  mounted () {
  window.scrollTo(0, 0)
  }
}
</script>

<style>
  #main {
    margin: 0 8px;
  }
</style>
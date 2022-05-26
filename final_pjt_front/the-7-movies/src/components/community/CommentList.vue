<template>
    
    <!-- <comment-list-form></comment-list-form> -->
    <div>
        <comment-list-item 
          v-for="comment in comments" 
          :comment="comment" 
          :key="comment.pk"
          >
        </comment-list-item>
    </div>
</template>

<script>
import CommentListItem from '@/components/community/CommentListItem.vue'
// import CommentListForm from '@/components/CommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentListItem },
  props: { comments: Array },
}
</script>

<style>
</style>
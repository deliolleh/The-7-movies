<template>
    
    <!-- <comment-list-form></comment-list-form> -->
    <v-container>
        <comment-list-item 
          v-for="comment in comments" 
          :comment="comment" 
          :key="comment.pk"
          >
        </comment-list-item>
    </v-container>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
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
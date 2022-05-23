<template>
  <li class="post">
    <router-link 
      class="user"
      :to="{ name: 'profile', params: { username: comment.user.username } }">
      {{ comment.user.username }}
    </router-link>
    
    <span v-if="!isEditing">{{ payload.content }}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <button @click="onUpdate">Update</button> |
      <button @click="switchIsEditing">Cancle</button>
    </span>

    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <button @click="switchIsEditing">Edit</button> |
      <button @click="deleteComment(payload)">Delete</button>
    </span>
     <div @click="likeComment(reviewPk)">
          <!-- Review Like UI -->
          <v-switch
            label="좋아요"
            hide-details
          ></v-switch>
      </div>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.comment.review,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    },
  },

}
</script>

<style scoped>
.user {
  width: 80px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #34495e;
  text-decoration: none;
}

a:hover {
  color: #2c3e50;
  text-decoration: underline;
}


.post {
  list-style: none;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #eee;
  justify-content: space-between;
}

</style>
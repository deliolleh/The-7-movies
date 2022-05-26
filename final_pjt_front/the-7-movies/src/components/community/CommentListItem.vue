<template>
    <v-card class="post">
      <router-link 
        class="user"
        :to="{ name: 'profile', params: { username: comment.user.username } }">
        {{ comment.user.username }}
      </router-link>

      <span v-if="!isEditing">{{ payload.content }}</span>

      <span v-if="currentUser.username === comment.user.username && !isEditing" class="float-right">
        <button @click="switchIsEditing">Edit</button> |
        <button @click="deleteComment(payload)">Delete</button>
      </span>

      <span v-if="isEditing">
        <input type="text" v-model="payload.content">
        <button @click="onUpdate">Update</button> |
        <button @click="switchIsEditing">Cancel</button>
      </span>

      <div @click="likeComment(payload)">
          <!-- Review Like UI -->
          <v-switch
            v-model="like"
            :input-value="like"
            label="좋아요"
            color="success"
            hide-details
            class="mx-2"
          ></v-switch>
      </div>
    </v-card>
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
      like: false,
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment', 'likeComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    checkLikes() {
      if (this.comment.like_people.includes(this.currentUser.pk)){
        this.like= true
        }
      },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    },
  },
  created() {
    this.checkLikes()
  }
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
  border-right: 1px #eee solid;
}

a:hover {
  color: #2c3e50;
  text-decoration: underline;
}


.post {
  width: 550px;
  list-style: none;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #eee;
  justify-content: space-between;
}

</style>
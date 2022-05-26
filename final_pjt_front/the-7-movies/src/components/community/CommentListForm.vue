<template>
  <div>

    <form @submit.prevent="onSubmit" class="comment-list-form">
      <label for="comment" class="pa-2">comment: </label>
      <input type="text" id="comment" v-model="content" required class="pr-2">
      <v-btn
      elevation="2"
      @click="onSubmit"
      > 등록 </v-btn>
    </form>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['review']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ reviewPk: this.review.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style scoped>

button {

}

form {
  display: flex;
  border-bottom: 1px solid #eee;
}

</style>
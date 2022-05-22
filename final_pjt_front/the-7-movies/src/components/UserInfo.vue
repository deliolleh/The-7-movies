<template>
  <div>
    <div>
      <i class="fa-solid fa-user"></i>
    </div>
    <div class="user-description">
      {{ profile.username }}
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'UserInfo',
  // props: {
  //   username: Object,
  // },
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username}
    this.fetchProfile(payload)
  }
}
</script>


<style scoped>
.user-container {
    display: flex;
    align-items: center;
  }

  .title {
    display: flex;
  }

  .content {
    display: flex;
    flex-direction: column;
  }

  .fa-user {
    font-size: 2.5rem;
  }

  .user-description {
    padding: 8px;
  }
</style>
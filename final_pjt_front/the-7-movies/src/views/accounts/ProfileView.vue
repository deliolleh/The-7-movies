<template>
  <div class="user-container">
    <user-info></user-info>
  </div>
</template>

<script>
import UserInfo from '@/components/accounts/UserInfo'

export default {
  name: 'ProfileView',
  components: {
    UserInfo,
  }
}
</script>

<style>

</style>
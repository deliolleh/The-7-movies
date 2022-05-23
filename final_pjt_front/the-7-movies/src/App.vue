<template>
  <div id="app">
    <nav-bar></nav-bar>
      <router-view></router-view>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import { mapActions } from 'vuex'
export default {
  name: 'HomeView',
  components: {
    NavBar,
  },
  methods: {
      ...mapActions(['fetchCurrentUser'])
    },
  created() {
    this.fetchCurrentUser()
  }
}
</script>

<style>

/* #app {
  display: flex;
  justify-content: center;
  align-items: center;
} */

</style>
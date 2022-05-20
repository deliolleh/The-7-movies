<template>
  <div>
    <nav-bar></nav-bar>
      <router-view></router-view>
      <the-practice></the-practice>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import { mapActions } from 'vuex'
import ThePractice from './components/thepractice.vue'
export default {
  name: 'HomeView',
  components: {
    NavBar,
    ThePractice,
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
</style>
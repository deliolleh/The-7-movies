<template>
  <v-app id="app">
    <nav-bar></nav-bar>
    <v-scroll-x-transition>
      <router-view></router-view>
    </v-scroll-x-transition>
  </v-app>
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
<template>
  <v-app id="app">
    <nav-bar></nav-bar>
    <transition name="fade" mode="out-in">
      <router-view></router-view>
    </transition>
    <the-spinner :loading="this.loadingStatus"></the-spinner>
    <the-footer></the-footer>
  </v-app>
</template>

<script>
import TheFooter from '@/components/common/TheFooter'
import NavBar from '@/components/common/NavBar.vue'
import { mapActions } from 'vuex'
import bus from '@/utils/bus'
// import TheSpinner from '@/components/common/TheSpinner'
export default {
  name: 'HomeView',
  components: {
    NavBar,
    // TheSpinner,
    TheFooter,
  },
  data() {
    return {
      loadingStatus: false
    }
  },
  methods: {
      ...mapActions(['fetchCurrentUser']),
      startSpinner() {
        this.loadingStatus = true
      },
      endSpinner() {
        this.loadingStatus = false
      }
  },
  created() {
    bus.$on('start:spinner', this.startSpinner)
    bus.$on('end:spinner', this.endSpinner)
    this.fetchCurrentUser()
  },
  beforeDestroy() {
    bus.$off('start:spinner', this.startSpinner)
    bus.$off('end:spinner', this.endSpinner)
  }
}
</script>

<style>

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}


.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* #app {
  display: flex;
  justify-content: center;
  align-items: center;
} */

</style>
<template>
    <v-footer
    dark
    padless
    color="#42b883"
    
  >
    <!-- <v-system-bar app style="height: 30px">
      <v-spacer></v-spacer>
    </v-system-bar> -->

      <v-card-text class="white--text text-center pa-0">
        {{ new Date().getFullYear() }} — <strong>The 7 Movies</strong>
        <small> created by 신혜원 한재혁 of 7th SSAFY </small>
      </v-card-text>
  </v-footer>
</template>

<script>
export default {
  name: 'TheFooter',
  data() {
    return {
      icons:[
          'mdi-facebook',
          'mdi-twitter',
          'mdi-linkedin',
          'mdi-instagram'
      ]
    }
  }
}
</script>

<style>
</style>
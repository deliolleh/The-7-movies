<template>
  <div>
    {{ recommends}}
  <the-spinner :loading="true"></the-spinner>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TheSpinner from '@/components/common/TheSpinner'
import bus from '@/utils/bus'

export default {
  name: 'AfterSelection',
  components: {
    TheSpinner,
  },
  computed: {
    ...mapGetters(['recommends'])
  },
  created() {
    bus.$emit('start:spinner')
    this.$store.dispatch('getRecommends')
  }
}
</script>

<style>

</style>
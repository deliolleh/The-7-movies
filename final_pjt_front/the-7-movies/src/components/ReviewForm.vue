<template>
  <div>
    <search-bar></search-bar>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import SearchBar from '@/components/SearchBar'
export default {
  name: 'ReviewForm',
  components: {
    SearchBar,
  },
  data() {
    return {
      movieInput: ''
    }
  },
  methods: {
    ...mapActions(['filteredList'])
  }
}
</script>

<style>

</style>
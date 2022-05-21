<template>
  <div>
    <router-link :to="{ name: 'reviewdatail', params: { reviewPk: item.id } } ">
      영화 제목 : {{ item.movie.title }} 제목 : {{ item.title }}
    </router-link>
    <!-- review 목록을 받아서 화면에 뿌리는 역할 -->
  </div>
</template>

<script>
// import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'ReviewListItem',
  props: {
    item: {
      type: Object,
    }
  }
}
</script>

<style>

</style>
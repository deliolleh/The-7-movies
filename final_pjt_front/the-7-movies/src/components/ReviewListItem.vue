<template>
  <v-card id="item">
    <div>
      <router-link style="text-decoration: none;" :to="{ name: 'reviewDatail', params: { reviewPk: item.pk } } ">
        {{ item.title }}
      </router-link>
      <div>
        <div><h5>{{ item.movie.title }}</h5></div>
      </div>
    </div>
    <div>
      <span>hi</span>
    </div>
    <!-- review 목록을 받아서 화면에 뿌리는 역할 -->
  </v-card>
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
  #item {
    padding: 1px 0 1px 20px;
  }
</style>
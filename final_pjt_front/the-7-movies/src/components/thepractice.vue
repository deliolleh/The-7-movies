<template>
  <div>
    <input v-model="findWord">
    <ul>
      <li v-for="(item, idx) in findItems" :key="idx">{{item}}</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ThePractice.view",
  data() {
    return {
      items:['설악산','한라산','북한산','백두산','지리산'],
      findWord:'',
    }
  },
  computed: {
      // this.findWord 가 변하면 그 문자가 포함된 리스트를 계산한다.
      findItems: function() {
          if (this.findWord) {
              return this.items.filter(function(value) {
                  return (value.indexOf(this.findWord) > -1);
              }, this);
          } else {
              // this.findWord 가 공백일땐 리스트를 그대로 반환한다.
              return this.items;
          }
      }
  }
}
</script>

<style>

</style>
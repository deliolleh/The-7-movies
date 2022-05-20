<template>
  <nav>
    <!-- 로고 및 홈화면 -->
    <div class="home">
      <router-link to="/">the-7-movies</router-link>
    </div>
    <!-- 화면 이동 like 커뮤니티, 추천등  -->
    <!-- <div>
      <router-link></router-link>
    </div> -->
    <!-- accounts 기능  -->
    <div class="users">
      <router-link :to="{name: 'login'}">Login</router-link>
      <router-link :to="{name: 'logout'}">Logout</router-link>
      <router-link :to="{name: 'signup'}">Signup</router-link>
      <router-link :to="{name : 'profile', params: {username} }">profile</router-link>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'NavBar',
  computed: {
    ...mapGetters(['currentUser']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
    }
  }

}
</script>

<style scoped>

nav {
  padding: 30px;
  display: flex;
  justify-content: space-between;
}

div a {
  font-weight: bold;
  color: #2c3e50;
  padding: 10px;
}

.home {
  display: flex;
}

.users {
  display: flex;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
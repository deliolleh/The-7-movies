<template>
  <v-container>
    <v-row>
      <v-col
        cols="12"
        sm="6"
        md="8"
      >
        <nav>
            <!-- 로고 및 홈화면 -->
            <div class="home">
              <img
              src="..\public\logo.png"
              style="width: 30px"
              >
              <router-link to="/">
                the-7-movies</router-link>
            </div>
            <!-- 화면 이동 like 커뮤니티, 추천등  -->
            <div class="community">
              <router-link :to="{name: 'community'}">Community</router-link>
            </div>
            <!-- accounts 기능  -->
            <div class="users">
              <div v-if="!isLoggedIn">
                <router-link :to="{name: 'login'}">Login</router-link>
                <router-link :to="{name: 'signup'}">Signup</router-link>
              </div>
              <div v-if="isLoggedIn">
                <router-link 
                  @click.native="logout"
                  :to="{name: 'logout'}">Logout</router-link>
                <router-link :to="{name : 'profile', params: {username} }">profile</router-link>
              </div>
            </div>
          </nav>
        </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters(['currentUser', 'isLoggedIn']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
    }
  },
  methods: {
    ...mapActions(['logout'])
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

.community {
  display: flex;
}

nav a.router-link-exact-active {
  color: #42b983;
}

a {
  color: #34495e;
  text-decoration: none;
}

a:hover {
  color: #2c3e50;
  text-decoration: underline;
}

a.router-link-exact-active {
  text-decoration: underline;
}

</style>
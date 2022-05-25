<template>
  <nav>
      <v-system-bar app style="height: 30px">
          <v-spacer></v-spacer>
      </v-system-bar>
      <v-app-bar app color="#42b883" class="mt-5">
          <img src="..\public\logo.png" style="width: 30px">
          <v-toolbar-title>
            <router-link to="/">
                  The-7-Movies
            </router-link>
          </v-toolbar-title>
          <router-link text class="ml-2" :to="{name: 'movieAll'}">Movies</router-link>
          <router-link :to="{name: 'community'}">Community</router-link>
          <router-link :to="{name: 'recommend'}">Recommends</router-link>
          <v-spacer></v-spacer>
          <v-autocomplete
          clearable
          hide-no-data
          hide-selected
          color="white"
          label="search"
          flat
          :items="movies"
          item-text="title"
          item-value="pk"
          id="search"
          >
            <template v-slot:item="{item}">
                <v-btn text :to="`/movies/${item.pk}`">{{item.title}}</v-btn>
            </template>
          </v-autocomplete>
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
          <v-badge bordered bottom color="green" dot offset-x="10" offset-y="10">
              <v-avatar size="40">
                  <!-- <v-img src="https://cdn.vuetifyjs.com/images/lists/2.jpg"></v-img> -->
              </v-avatar>
          </v-badge>
      </v-app-bar>
  </nav>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters(['currentUser', 'isLoggedIn', 'movies']),
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

.header {
    color: white;
    background-color: #42b883;
    display: flex;
    padding: 8px;
}
.header .router-link-exact-active {
    color: #35495e;
}


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
  color: #34495e;
}

a {
  color: white;
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
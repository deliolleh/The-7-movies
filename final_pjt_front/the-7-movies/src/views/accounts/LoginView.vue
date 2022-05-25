<template>
  <div>

    <account-error-list v-if="authError"></account-error-list>
    <div class="form-container sign-in-container mt-12 d-flex">
      <v-form ref="form"       
        @submit.prevent="login(credentials)"
        class="px-2, px-8"
        >
        <img src="team.png" class="team-img pt-8" />
        <h1 class="pb-8 font-weight-bold">Sign in</h1>
        <v-text-field
        prepend-inner-icon="mdi-account"
        v-model="credentials.username"
        label="Username"
        required
        ></v-text-field>
        <v-text-field
        prepend-inner-icon="mdi-lock"
        v-model="credentials.password"
        label="Password"
        type="password"
        required
        >
        </v-text-field>
        <v-btn
        :disabled="!credentials.password"
        type="submit"
        color="success"
        class="pa-6 font-weight-bold mr-4"
        elevation="0"
        block
        dark
        tile
        >
        Sign in
        </v-btn>
      </v-form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'
  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        },
      }
    },
  computed: {
      ...mapGetters(['authError', 'isValid'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style>

#app > div > div:nth-child(2) {
  display: flex;
  justify-content: center;
}

#app > div > div:nth-child(2) > div > form > button {
  background-color: #42b883!important
}

.sign-in-container {
  left: 0;
  width: 50%;
  z-index: 2;
}
.team-img {
  width: 50%;
}

.container.right-panel-active .sign-in-container {
  transform: translateX(100%);
}


</style>
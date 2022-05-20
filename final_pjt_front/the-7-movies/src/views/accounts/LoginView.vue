<template>
  <div>
    <h1>Login</h1>

    <account-error-list v-if="authError"></account-error-list>
    
    <v-form ref="form"       
      @submit.prevent="login(credentials)"
      >
      <v-text-field
      v-model="credentials.username"
      label="Username"
      required
      ></v-text-field>
      <v-text-field
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
      class="mr-4"
      >
      로그인
      </v-btn>
    </v-form>
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

.theme--light.v-btn.v-btn--has-bg {
  background-color: #42b883!important
}

</style>
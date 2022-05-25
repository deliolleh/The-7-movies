<template>
  <div>

    <account-error-list v-if="authError"></account-error-list>
    <div class="form-container sign-up-container mt-12 d-flex">
      <v-form
        ref="form"
        class="px-8 px-2"       
        @submit.prevent="signup(credentials)"
        >
        <img src="team.png" class="team-img" />
        <h1 class="pb-12 font-weight-bold">Create Account</h1>
        <v-text-field
        v-model="credentials.username"
        prepend-inner-icon="mdi-account"
        label="Username"
        required
        ></v-text-field>
        <v-text-field
        v-model="credentials.password1"
        prepend-inner-icon="mdi-lock"
        type="password"
        label="비밀번호"
        required
        >
        </v-text-field>
        <v-text-field
        v-model="credentials.password2"
        prepend-inner-icon="mdi-lock"
        label="비밀번호 확인"
        type="password"
        required
        >
        </v-text-field>
        <v-btn
        :disabled="!credentials.password2"
        type="submit"
        color="success"
        class="pa-6 font-weight-bold mr-4"
        block
        dark
        tile
        >
        Sign up
        </v-btn>
      </v-form>
  </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style>

#app > div > div:nth-child(2) {
  display: flex;
  justify-content: center;
}

.sign-up-container {
  left: 0;
  width: 50%;
  z-index: 2;
}
.team-img {
  width: 50%;
}

.container.right-panel-active .sign-up-container {
  transform: translateX(100%);
}


</style>

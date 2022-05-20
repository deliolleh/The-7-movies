<template>
  <div>
    <h1>회원가입</h1>
    <br>
    <v-form 
      ref="form"       
      @submit.prevent="signup(credentials)"
      >
      <v-text-field
      v-model="credentials.username"
      label="Username"
      required
      ></v-text-field>
      <v-text-field
      v-model="credentials.password1"
      type="password"
      label="비밀번호"
      required
      >
      </v-text-field>
      <v-text-field
      v-model="credentials.password2"
      label="비밀번호 확인"
      type="password"
      required
      >
      </v-text-field>
      <v-btn
      :disabled="!credentials.password2"
      color="success"
      class="mr-4"
      >
      회원 가입
      </v-btn>
    </v-form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'


  export default {
    name: 'SignupView',
    components: {
      
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
h1 {
  text-align: center;
}
</style>

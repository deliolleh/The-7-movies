<template>
  <v-app>
    <v-row
    justify="center"
    >
      <v-card
      id="cards"
      >
        <v-card-title>
          <i class="fa-solid fa-user mx-5 my-5"></i>
            {{ profile.username }}
        </v-card-title>
        <hr>
        <br>
        <div
        v-if="profile.review_set.length"
        >
          <ul>
            <h2> 작성 글 목록 </h2>
            <li
            :v-for="(review, idx) in profile.review_set"
            :key="idx"
            >
              {{ review }}
            이건 그냥 텍스트
              <router-link :to="{name: 'reviewDatail', params: {reviewPk: pk}}">
              
              </router-link>
            </li>
          </ul>
        </div>
        
        <div v-else>
          <span class="mx-5">
            아직 작성한 글이 없으시네요.
          </span>
          
          <router-link :to="{name: 'create'}">
            <v-btn> 글쓰러 가기 </v-btn>
          </router-link>
        </div>
        <div class="mx-5">
          이런 영화는 어떠세요?
          <p>
            <router-link :to="{name: 'movieDetail', params:{moviePk: recommends[0].pk}}">
              {{ recommends[0].title }}
              <small> 보러 가기 </small>
            </router-link>
          </p>
        </div>

        <v-card-text>

        </v-card-text>
        <div class="user-description">
        </div>
      </v-card>
    </v-row>
  </v-app>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'UserInfo',
  // props: {
  //   username: Object,
  // },
  computed: {
    ...mapGetters(['profile', 'recommends'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  // created() {
  //   this.fetchProfile(this.$route.params.username)
  // }
}
</script>


<style scoped>
.user-container {
    display: flex;
    align-items: center;
  }

  .title {
    display: flex;
  }

  .content {
    display: flex;
    flex-direction: column;
  }

  .fa-user {
    font-size: 2.5rem;
  }

  .user-description {
    padding: 8px;
  }

  #cards {
    width: 450px;
    height: 450px;
  }

  a {
  text-decoration: none;
}

a:hover {
  color: #2c3e50;
  text-decoration: underline;
}

a.router-link-exact-active {
  text-decoration: underline;
}

ul {
  list-style: none;
}
</style>
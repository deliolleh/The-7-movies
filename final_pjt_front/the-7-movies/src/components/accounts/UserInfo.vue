<template>
  <v-container align="center" justify="center" class="mt-5">
    <h1 class="mx-3 text-center">
      {{ profile.username }}'s profile
    </h1>
    <v-row
    justify="center"
    align="center"
    >
      <v-card
      id="cards"
      height="auto"
      >
        <v-card-title>
          <i class="fa-solid fa-user mx-5 my-5"></i>
            {{ profile.username }}
        </v-card-title>
        <v-spacer></v-spacer>
        <v-card-text>
        <v-divider inset></v-divider>
                <div class="font-weight-bold ml-8 mb-2">
                  User Details
                </div>
                <v-list two-line>
                  <v-list-item>
                    <v-list-item-icon>
                      <v-icon color="indigo">
                        mdi-pen
                      </v-icon>
                    </v-list-item-icon>
                    <v-list-item-content v-if="profile.review_set.length">
                      <v-list-item-title
                        :key="idx"
                        >작성글 목록
                        </v-list-item-title>
                        <div v-for="(review, idx) in profile.review_set" :key="idx">
                          <router-link :to="{name: 'reviewDatail', params: {reviewPk: review.pk}}">
                          <v-list-item-subtitle>{{ review.title }}</v-list-item-subtitle>
                          </router-link>
                        </div>
                    </v-list-item-content>
                      <v-list-item-content v-else>
                      <v-list-item-title> 아직 작성한 리뷰가 없네요! </v-list-item-title>              
                      <router-link :to="{name: 'create'}">
                      <v-list-item-subtitle> 리뷰 쓰러 가기 </v-list-item-subtitle>
                      </router-link>
                    </v-list-item-content>
                  </v-list-item>

                  <v-divider inset></v-divider>

                  <v-list-item>
                    <v-list-item-icon>
                      <v-icon color="indigo">
                        mdi-video
                      </v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                      <v-list-item-title>{{ profile.username }}님의 취향저격 영화</v-list-item-title>
                      <v-list-item-subtitle><router-link :to="{name: 'movieDetail', params:{moviePk: recommends[0].pk}}">
                        {{ recommends[0].title }}
                        <small> 보러 가기 </small>
                        <v-img 
                        :src="recommends[0].poster_path"
                        style="width: 100px"
                        ></v-img>
                        </router-link></v-list-item-subtitle>
                    </v-list-item-content>
                  </v-list-item>

                </v-list>
              </v-card-text>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
// import bus from '@/utils/bus'

export default {
  name: 'UserInfo',
  // props: {
  //   username: Object,
  // },
  computed: {
    ...mapGetters(['profile', 'recommends']),
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    this.fetchProfile(this.$route.params.username)
    console.log(this.profile.review_set)
  },
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
    width: 500px;
    height: 650px;
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
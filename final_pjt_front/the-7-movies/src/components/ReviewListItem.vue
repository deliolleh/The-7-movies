<template>
  <v-container>
    <v-spacer></v-spacer>
    <v-row>
      <v-col
        sm="3"
        md="2"
        >
      </v-col>
      <v-col
        cols="12"
        sm="6"
        md="8"
      >
        <v-card id="item">
          <ul class="review-list">
            <li class="post">
              <div> 
                <router-link class="username" :to="{ name: 'profile', params: { username: item.user.username } } ">
                  Reviewer : {{ item.user.username }} 
                </router-link>
              </div>
              <div>
                <p class="review-title">
                  <router-link style="text-decoration: none;" :to="{ name: 'reviewDatail', params: { reviewPk: item.pk } } ">
                    {{ item.title }}
                  </router-link>
                </p>
              </div>
            </li>
          </ul>
          <div>
            <div class="movie-title">
              <router-link style="text-decoration: none;" :to="{name: 'movieDetail', params: {moviePk : item.movie.pk} }">
                <h5>영화 제목 : {{ item.movie.title }}</h5>
              </router-link>
            </div>
          </div>
          <div>
            <span>{{  }}</span>
          </div>
          <!-- review 목록을 받아서 화면에 뿌리는 역할 -->
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'
// import { mapActions, mapGetters } from 'vuex'
export default {
  name: 'ReviewListItem',
  props: {
    item: {
      type: Object,
    }
  },
  computed: {
    ...mapGetters(['currentUser'])
  }
}
</script>

<style scoped>
#item {
  padding: 1px 0 1px 20px;
}

.review-list {
  margin: 0;
  padding: 0;
}

.review-title {
  margin: 10px;
  text-align: center;
}

.post {
  list-style: none;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #eee;
}

.username {
  width: 200px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #42b883;
  border-right: whitesmoke solid;
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

.movie-title {
  width: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>
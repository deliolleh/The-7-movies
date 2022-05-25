<template>
  <v-container>
    <v-row>
      <v-col
        cols="1"></v-col>
      <v-col
        cols="10">
        <div v-for="(review, idx) in bestReviews" :key="idx">
          <v-card id="item">
            <ul class="review-list">
              <li class="post">
                <div>
                  <router-link class="username" :to="{ name: 'profile', params: { username: review.user.username } } ">
                      글쓴이 : {{ review.user.username }} 
                    </router-link>
                </div>
                <div class="review-title">
                  <router-link style="text-decoration: none;" :to="{ name: 'reviewDatail', params: { reviewPk: review.pk } } ">
                    {{ review.title }}
                  </router-link>
                </div>
              </li>
            </ul>
          </v-card>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'BestReview',
  computed: {
    ...mapGetters(['bestReviews'])
  },
  methods: {
    ...mapActions(['getBestReview']),
  },
  created() {
    this.getBestReview(this.$route.params.moviePk)
    // console.log(this.movie)
  }
}
</script>

<style>
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
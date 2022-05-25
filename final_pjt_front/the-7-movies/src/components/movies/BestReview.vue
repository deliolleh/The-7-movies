<template>
  <div>
    <v-row>
      <v-col
        v-for="(review, idx) in bestReviews" :key="idx"
        cols="3"
        >
        <v-card>
          <v-card-title
            class="text-subtitle-1">
            Reviewer : {{ review.user.username }}
          </v-card-title>
          <v-card-text>
            {{ review.title }}
          </v-card-text>
          <v-card-actions>
            <v-btn
              text
              color="teal accent-4"
              @click="reveal = true"
            >
              Read content
            </v-btn>
          </v-card-actions>
          <v-expand-transition>
            <v-card
              v-if="reveal"
              class="transition-fast-in-fast-out v-card--reveal"
              style="height: 100%;"
            >
              <v-card-text class="pb-0">
                <p>{{ review.content }} </p>
              </v-card-text>
              <v-card-actions class="pt-0">
                <v-btn
                  text
                  color="teal accent-4"
                  @click="reveal = false"
                >
                  Close
                </v-btn>
                <v-btn
                  text
                  color="teal accent-4"
                  :to="{name: 'reviewDatail', params:{reviewPk: review.pk} }"
                >
                  See detail...
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-expand-transition>
        </v-card>
      </v-col>
    </v-row>
  </div>
  <!-- <v-container>
    <v-row>
      <v-col
        cols="1"></v-col>
      <v-col
        cols="10">
        <div v-for="(review, idx) in bestReviews" :key="idx">
          <v-card id="item" style="width:300px">
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
  </v-container> -->
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'BestReview',
  data() {
    return {
      reveal: false,
    }
  },
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

<style scoped>
.v-card--reveal {
  bottom: 0;
  opacity: 1 !important;
  position: absolute;
  width: 100%;
}

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
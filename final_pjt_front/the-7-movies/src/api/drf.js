const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const COMMUNITY = 'community/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + `${username}/`,
    init: () => HOST + ACCOUNTS + 'genre_init/',
    changeUserInfo: () => HOST + ACCOUNTS + 'get_init/'
  },
  // articles: {
  //   // /articles/
  //   articles: () => HOST + ARTICLES,
  //   // /articles/1/
  //   article: articlePk => HOST + ARTICLES + `${articlePk}/`,
  //   likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
  //   comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
  //   comment: (articlePk, commentPk) =>
  //     HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  // },
  movies: {
    search: () => HOST + MOVIES + 'review/search/',
    recommend: () => HOST + MOVIES + 'recommends/representative/', //이상형
    detail: moviePk => HOST + MOVIES + `${moviePk}/`,
    best: () => HOST + MOVIES + 'popular/',
    recommends: () => HOST + MOVIES + 'recommends/' //유저 추천영화
  },
  community: {
    reviews: () => HOST + COMMUNITY,
    create: () => HOST + COMMUNITY + 'create/',
    detail: reviewPk => HOST + COMMUNITY + `${reviewPk}/`,
    likereview: reviewPk => HOST + COMMUNITY + `${reviewPk}/` + 'like/',
    comments: reviewPk => HOST + COMMUNITY + `${reviewPk}/` + 'comment/',
    likecomment: (reviewPk, commentPk) => HOST + COMMUNITY + `${reviewPk}/` + `${commentPk}/` + 'like/',
    updateDelete: (reviewPk, commentPk) => HOST + COMMUNITY + `${reviewPk}/` + `${commentPk}/`,
  }
}

# 관통프로젝트

### api url

- base_url = 'api/v1'

- coummunity
  - `''`: views.review_list_or_create
  - `<int:review_pk>/`: review_detail_or_update_or_delete
  - `<int:review_pk>/like/`: like_review
  - `<int:review_pk>/comments/`: create_comment
  - `<int:review_pk>/comments/<int:comment_pk>/`: comment_update_or_delete



- moives
  - `''`: movie_list
  - `<int:movie_pk>/`: movie_detail



- accounts
  - `<username>`: profile



### Vue URL

- 

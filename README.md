# Final_PJT README

## 조원

- 한재혁
  - Back Main

<br>

- 신혜원
  - Front Main

<br>

---

## 구현

- 목표 구현: 영화들에 대한 유저의 평점에 따라, 유저의 장르별 선호도 수치를 저장하고, 이를 활용하여 유저에게 현재의 선호도가 높은 영화들을 추천
- 실제 구현:

<br>

---

## ERD

![image-20220526094550317](README.assets/image-20220526094550317.png)

<br>

---

## 필수기능

- 메인화면 첫 영화 caroseul
  - DB에 저장되어있는 영화들 중 영화 평점을 남긴 유저 수가 많은 영화들 일부를 추려내어 출력하게 했습니다
- 메인화면/ Recommends, **The 7 Movies for You**
  - 유저의 장르 status에서 점수가 가장 높은 장르들을 뽑아온 뒤, 해당 장르에서 평점이 높은 영화들을 일정 수만큼 선택한 후, 중복을 제거하고 영화를 출력하도록 함
- 상세 영화 정보
  - 영화의 제목, 감독, 개봉일, 평점, 장르가 표시되고, 해당 영화에 대한 유저의 평점을 등록할 수 있으며, 이를 리셋할 수도 있습니다.
  - 상세 정보에서 바로 review 작성으로 넘어갈 수 있으며, 이 때는 moive의 정보도 함께 넘어가, 자동으로 영화제목에 등록이 됩니다. 

- Movies
  - DB에 저장된 모든 영화들을 출력합니다
  - Infinite Scroll을 지원합니다
  - 영화를 클릭시 상세 영화 정보로 넘어갑니다
- Community
  - 모든 Review들이 출력됩니다
  - Pagination이 사용되었습니다
  - 유저, 제목, 영화 제목을 클릭하면 각각, 유저 프로필, 리뷰 상세, 영화 상세로 이동합니다
- 상세 리뷰 정보
  - 본문은 유저이름, 제목, 내용으로 구성되어있습니다
  - 리뷰에 대한 좋아요가 가능합니다
  - 댓글 생성이 가능하며, 댓글 좋아요도 가능합니다
- profile
  - 본인이 작성한 글 제목이 나오고, 클릭시 해당 리뷰로 넘어갑니다
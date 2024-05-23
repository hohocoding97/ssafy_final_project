# ssafy_final_project
ssafy final project

## 팀원 정보 및 업무 분담
### 탁호준
- 팀장
- 
## 설계 내용 및 실제 구현 정도

## 데이터베이스 모델링


## 


## API 명세서



## tmdb 영화 정보가져오기


## Dj-Rest-Auth 설치 및 사용
`pip install dj-rest-auth`

#### 토큰 보내기
headers에 Authorization 값에 token값을 넣어서 넣어줘야함

키를 보낼때 앞에 접두사 `Token`작성 후 한 칸 띄어쓰기 후 token값이 들어가야함


# Takofix

### 팀 구성

팀장 - 탁호준 (FullStack)
팀원 - 이남경 (Front-End)

### 프로젝트 목표

타코야끼를 컨셉으로한 영화 정보 제공 사이트 제작
사용자가 영화 정보 뿐만 아니라 다양한 재미를 얻을 수 있도록 게임적 요소, 참여적 요소 추가

### 개발 일정

개발 기간 : 2024.05.08 - 2024.05.24

![](https://velog.velcdn.com/images/lurelight/post/5ea7cb87-7fb4-461a-8597-74b9bdcb5c0b/image.png)

### 기반 작업

**데이터 ERD**

![](https://velog.velcdn.com/images/lurelight/post/e92cda83-fc47-4138-8fd2-d9b966089263/image.png)

**APP**

![](https://velog.velcdn.com/images/lurelight/post/0b1ced2a-c694-4109-a37c-62c44169f96f/image.png)

**MODEL**

![](https://velog.velcdn.com/images/lurelight/post/bb22fde7-0974-4b58-9db5-3d2e7742f2c6/image.png)

**API 명세서**

![](https://velog.velcdn.com/images/lurelight/post/07162e80-4e1b-44b3-ac4f-1dbcbc8a9815/image.png)
![](https://velog.velcdn.com/images/lurelight/post/e65ccd72-0aec-4fbc-90de-cc68659fcf57/image.png)
![](https://velog.velcdn.com/images/lurelight/post/40e6802b-d845-41a1-bd49-9519dbe86c48/image.png)

#### 디자인 레이아웃 설계

**Main Page**

![](https://velog.velcdn.com/images/lurelight/post/c0e61c3a-976d-4ac2-b1b4-2deb8a29a3f5/image.png)

**Search Page**

![](https://velog.velcdn.com/images/lurelight/post/98608fee-389a-4da7-8d9d-2cb4eb9114bd/image.png)

**Search Page (Unknown)**

![](https://velog.velcdn.com/images/lurelight/post/108d74cf-4cdc-4ba2-a843-c0d89528730e/image.png)

**AI Recommend Page**

![](https://velog.velcdn.com/images/lurelight/post/e4559a6f-dd50-4fca-8c3f-dcebfa1fed9d/image.png)

**AI Recommend Page (Result)**

![](https://velog.velcdn.com/images/lurelight/post/3552b2b8-a447-4500-9916-492dcafc8fb9/image.png)

**Login Page**

![](https://velog.velcdn.com/images/lurelight/post/ef88d65d-82fd-4025-8714-111ab20e482d/image.png)

**Sign Up Page**

![](https://velog.velcdn.com/images/lurelight/post/42a2a5d4-fd4f-47d0-8fcf-12fd903dcbb2/image.png)

**Article Detail Page**

![](https://velog.velcdn.com/images/lurelight/post/580834e1-4e8d-4bd4-b982-ef09d90bf77d/image.png)

**Article Create Page**

![](https://velog.velcdn.com/images/lurelight/post/f7b34702-12e8-448c-84cb-f1e5d94f88a0/image.png)

**Community Page**

![](https://velog.velcdn.com/images/lurelight/post/7c258f21-0ad8-4f59-b922-4f6f8d896248/image.png)

**Movie Detail Page**

![](https://velog.velcdn.com/images/lurelight/post/4aa71615-1e9e-4a2d-8f90-789bd472a412/image.png)

**TakoTalk Page**

![](https://velog.velcdn.com/images/lurelight/post/827a6f76-e20f-46da-982d-fd44952184c5/image.png)

**TakoTalk Page (Detail)**

![](https://velog.velcdn.com/images/lurelight/post/91244308-9738-47df-b037-26a6d0399da9/image.png)

**Profile Page**

![](https://velog.velcdn.com/images/lurelight/post/d22a1c7a-d51b-4d7a-b28e-c77a7025f544/image.png)

**Edit Profile Page**

![](https://velog.velcdn.com/images/lurelight/post/477301b5-0edc-4b0b-853f-f9783dcc3ea4/image.png)

**Delete Profile Page**

![](https://velog.velcdn.com/images/lurelight/post/b41a4d4f-3b8e-436d-848d-6e55865bf347/image.png)

## 구현 기능

**Random Movie 선택 기능**

![](https://velog.velcdn.com/images/lurelight/post/c81d64ba-58b7-4bcc-8ce8-afcc718eadd1/image.png)

- 빨간 버튼 클릭 시 매번 새로운 영화가 나타남
- 해당 영화에 대한 상세정보를 알고싶은 경우, 영화 포스터를 클릭하면 Detail Page로 넘어갈 수 있음

**장르별 추천 영화 선택 기능**

![](https://velog.velcdn.com/images/lurelight/post/6320ee1e-1860-4b0e-a44a-225edd263a8a/image.png)

- 원하는 장르 버튼을 클릭하면 해당 장르와 연관된 영화들만 화면에 나타남

**영화 carousel 기능**

![](https://velog.velcdn.com/images/lurelight/post/4b4f086d-2988-4fc9-b944-049028c7352a/image.png)

- splide 기능을 설치하여 영화 포스터들이 carousel 형태로 나타나도록 함
- 좌, 우 버튼을 눌러도 동작하지만, 일정 시간이 지나면 자동적으로 포스터가 이동함

**community 기능**

![](https://velog.velcdn.com/images/lurelight/post/b4107fe9-27c4-47bf-8cc8-93e3489aa218/image.png)

- 영화에 대한 후기/정보 등을 공유할 수 있는 게시판 모음
- 특정 게시글을 클릭하면 해당 글의 상세 정보를 확인할 수 있음
- 글쓰기 버튼 클릭 시 새로운 게시글을 적을 수 있음. 비회원일 경우는 로그인이 필요하다는 경고창이 뜸

**article 기능**

![](https://velog.velcdn.com/images/lurelight/post/ba1dbdb7-2a6a-4ba6-bb28-d40d44fe8161/image.png)

![](https://velog.velcdn.com/images/lurelight/post/69e12166-5ec0-4df9-a416-1444886ad62b/image.png)

- 게시글에 적고싶은 내용(공백 금지)을 적고 등록 버튼을 누르면 새로운 게시글이 작성됨
- 글을 작성한 작성자는 자신이 적은 글을 삭제/수정할 수 있음
- 사용자들은 누군가의 게시글에 자유롭게 댓글을 달 수 있음

**Search 기능**

![](https://velog.velcdn.com/images/lurelight/post/2b27a0b2-5e43-4db9-94c3-7eae66870bad/image.png)

![](https://velog.velcdn.com/images/lurelight/post/520786cd-d4e9-4e97-99a3-615af637e7bf/image.png)

![](https://velog.velcdn.com/images/lurelight/post/f2ec0889-a128-472e-98ef-c87acf66e9c9/image.png)

- 특정 키워드를 검색시 관련된 영화/배우에 대한 정보가 출력됨
- 만약 검색어가 없을 경우 3번째 사진처럼 관련 내용을 찾을 수 없다는 결과가 나옴

**Profile 기능**

![](https://velog.velcdn.com/images/lurelight/post/6bb22b24-9997-4d8c-93fb-d5f9fad639dc/image.png)

- 사용자의 이름과 팔로잉/팔로우 수가 나타남
- 사용자가 선호하는 영화도 확인할 수 있음

**Movie Detail 기능**

![](https://velog.velcdn.com/images/lurelight/post/28012cf2-4718-4f60-94fd-7455c52293d2/image.png)

- 영화와 관련된 정보가 출력됨
- TMDB에서 얻은 평점에 대한 정보들을 원형으로 나타냄
- 하트 버튼을 클릭하면 해당 영화에 대한 좋아요를 표시할 수 있음
- 영화 정보 뿐만 아니라 영화에 출연한 배우들에 대한 정보도 함께 알 수 있음

**Sign Up 기능**

![](https://velog.velcdn.com/images/lurelight/post/88ccea68-9cad-4ccf-965a-9b0072b65e7b/image.png)

- ID, PASSWORD를 입력해 사용자 계정 생성 가능

**Login 기능**

![](https://velog.velcdn.com/images/lurelight/post/26ddcbde-0603-45c6-9baf-dac472cb69fb/image.png)

- 생성한 사용자 정보를 바탕으로 로그인 기능 구현


### 소감 & 느낀점

탁호준(FULL-STACK) 

이번 영화 추천 사이트 제작 프로젝트를 진행하면서 기록의 중요성을 가장 많이 느꼈습니다. 프로젝트 진행 중에 어려웠던 부분들을 개발자 일지에 적으며 하니 비슷한 문제에 직면했을 때, 비교적 쉽게 해결할 수 있었습니다. 또 API 명세서를 작성해서 어떤 url로 어떤 method로 요청을 보내야 하는지 다시 찾아보는데 시간이 줄었던 것 같습니다. 처음에는 컴포넌트를 어떻게 구성해야할지 감이 잘 잡히지 않았는데, 프로젝트를 진행하며 많이 배우게 되었습니다. Chat GPT를 이용해 사용자가 좋아할 만한 영화들을 추천받아서 사용하고 싶었지만 시간이 부족해서 진행하지 못했던 게 조금 아쉬웠습니다. 

이남경 (FRONT-END)

Vue.js를 활용해 처음으로 사이트를 제작했습니다. Vue.js의 다양한 기능과 문법들을 활용하여 프로젝트를 구현하며 개발하는 경험이 신선했습니다. 특히 Vue의 컴포넌트를 활용하여 아키텍쳐 코드를 구조화한 점이 코드들을 깔끔하게 정리하는데 많은 도움이 되었던 것 같습니다. Vue.js에 대해 더 많이 배우는 좋은 경험이었습니다. 향후 Vue.js를 활용해 Front-end, Design 쪽으로 나아가는 좋은 기반이 되었습니다.


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


## ChatGPT API를 이용한 영화 추천
### 1. 유저가 좋아하는 영화 및 장르 입력
![유저 입력 창](/md_imgs/user_input_form.png)


### 2. 프롬프트 및 답변
```
사용자가 좋아할 만한 영화를 추천해줘
탁호준 유저가 좋아하는 영화는
"비긴 어게인", "과속 스캔들", "너의 이름은" 이야.
탁호준 유저가 좋아하는 장르는 
"로맨스", "코미디", "액션" 장르야.
답변을 줄때 내가 알려준 예시와 같은 형태로 줘
[{name: '스타워즈 에피소드 4: 새로운 희망', movie_code : 11}, {name: 터미네이터, movie_code : 217 }, ]

이때 name은 영화 제목이야
movie_code는 tmdb 사이트에서 정한 영화 ID야 
```

```
[{name: '라라랜드', movie_code: 313369}, {name: '어바웃 타임', movie_code: 122906}, {name: '나의 소녀시대', movie_code: 342521}, {name: '노트북', movie_code: 11036}, {name: '어벤져스', movie_code: 24428}]
```

### 3. 답변 처리
tmdb api를 이용해 movie_code를 이용해 영화 디테일 정보를 axios를 받아와서 유저에게 보여주기

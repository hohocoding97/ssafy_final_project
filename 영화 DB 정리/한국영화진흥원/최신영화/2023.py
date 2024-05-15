import requests
import json

# API 키
api_key = "c749cadac1d9f0a8006aa2267c7210e2"

# 기본 요청 URL
base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"

# 요청 변수 설정
payload = {
    "key": api_key,
    "curPage": "1",  # 현재 페이지
    "itemPerPage": "70",  # 결과 ROW의 개수
    "openStartDt": "2023",  # 조회시작 개봉연도
    "openEndDt": "2023"  # 조회종료 개봉연도
}

# API 호출
response = requests.get(base_url, params=payload)

# 응답 데이터 확인
data = response.json()

# 영화 목록만 추출
movies = data.get("movieListResult").get("movieList")

# JSON 파일로 저장
with open('2023_movies.json', 'w', encoding='utf-8') as f:
    json.dump(movies, f, ensure_ascii=False, indent=4)

print("JSON 파일이 생성되었습니다.")

import requests
import json

# KOFIC API 키
API_KEY = "c749cadac1d9f0a8006aa2267c7210e2"

# API 요청을 위한 URL
url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={API_KEY}&openStartDt=2023"

# API 요청 보내기
response = requests.get(url)

# 응답 데이터 확인
data = response.json()

# 데이터를 JSON 파일로 저장
with open('movies_2023.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("2023년에 개봉한 영화 데이터가 성공적으로 저장되었습니다.")

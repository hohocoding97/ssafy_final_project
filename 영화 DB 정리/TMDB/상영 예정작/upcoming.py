import requests
import json

# TMDb API 키
API_KEY = "851b281891fdbce4fc703fe71e8e1bdc"

# API 엔드포인트
url = f"https://api.themoviedb.org/3/movie/upcoming?api_key={API_KEY}&language=ko-KR&page=1"

# API 요청 보내기
response = requests.get(url)

# 응답 데이터 확인
data = response.json()

# 데이터를 JSON 파일로 저장
with open('movies_upcoming.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("영화 데이터가 성공적으로 저장되었습니다.")

import requests
import json

# API 키
api_key = "c749cadac1d9f0a8006aa2267c7210e2"

# 기본 요청 URL
base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"

# 요청 변수 설정
payload = {
    "key": api_key,
    "targetDt": "20240510",  # 조회하고자 하는 날짜 (예시 날짜)
    "weekGb": "0",  # 주간 (월~일)
    "itemPerPage": "10",  # 결과 ROW의 개수
    "multiMovieYn": "N",  # 상업영화
    "repNationCd": "K",  # 한국영화
    "wideAreaCd": ""  # 전체 지역
}

# API 호출
response = requests.get(base_url, params=payload)

# 응답 데이터 확인
data = response.json()

# JSON 파일로 저장
with open('box_office_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("JSON 파일이 생성되었습니다.")

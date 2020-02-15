import requests
import pandas as pd
import time
import os


# 구글 map API 장소 좌표 찍고 그 주변 반경 검색하기
# 잘 사용하면 괜춘할듯 ex) 자기 좌표 찍고 그 주변 경매 물건 확인하기


# 요철할 주소
site = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

# 요철할때 서버로 전달할 파라미터 데이터
param_dict = {
    'key': 'AIzaSyDIKE0ZV_Z8lERPEP7RmRffVBHnTueCLys',
    'location': '37.501528,127.039585',
    'radius': '1000',
    'language': 'ko',
    'type': 'bank'

}

# 요첳한다.
response = requests.get(site, params=param_dict)
print(response)

while True:
    time.sleep(1)
    # JSON 문서를 분석한다.
    root = response.json()

    # 데이터를 추출한다.
    if root['status'] == 'OK':
        # results 라는 이름으로 저장되어 있는 리스트의 수만큼 반복
        for result in root["results"]:
            # 데이터 추출
            lat = result['geometry']['location']['lat']
            lng = result['geometry']['location']['lng']
            name_str = result['name']
            vicinity = result['vicinity']

            # print(lat, lng, name_str, vicinity)

            df1 = pd.DataFrame([[lat, lng, name_str, vicinity]])

            # 파일이 없다면 헤더까지 같이 저장한다.
            if os.path.exists('google_api_data.csv') == False:
                df1.columns = ['lat', 'lng', 'name', 'vicinity']
                df1.to_csv('google_api_data.csv', index=False, encoding='utf-8-sig')
            else:
                df1.to_csv('google_api_data.csv', index=False, encoding='utf-8-sig', mode='a', header=False)

    # 다음 페이지가 있다면 다음 페이지 정보를 요청한다.
    if 'next_page_token' in root:
        print('수집중')
        next_dict = {
            'key': 'AIzaSyDIKE0ZV_Z8lERPEP7RmRffVBHnTueCLys',
            'pagetoken': root['next_page_token']
            'language': 'ko'
        }
        response = requests.get(site, params=next_dict)
    else:
        print('수집완료')
        break


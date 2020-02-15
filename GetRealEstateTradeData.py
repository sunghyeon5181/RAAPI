from base64 import encode, decode
from urllib.request import Request, urlopen
from numpy.core import unicode



input ='인천 강화'
input2 = "201512"
inputs = input.split(' ')
sido = str(inputs[0].encode('utf-8'))
gungo =str(inputs[1].encode('utf-8'))
# munli =str(inputs[2])
# number=str( inputs[3])
# dong =str( inputs[4])
# ho =      str( inputs[5])

url = "http://openapi.1365.go.kr/openapi/service/rest/CodeInquiryService/getAreaCodeInquiryList?schSido="+sido+"&schGugun="+gungo

urlEx = "http://openapi.1365.go.kr/openapi/service/rest/CodeInquiryService/getAreaCodeInquiryList?schSido=%EC%84%9C%EC%9A%B8&schGugun=%EC%A2%85%EB%A1%9C"

request = Request(urlEx)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)


# 코드값 가져오기



# 진짜 URL 던지기

code = response_body 중에 지역코드를 짤라냄



url = "~~ KK "+ code + input2


request = Request(url)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()

response_body.t


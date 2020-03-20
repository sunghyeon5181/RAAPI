# 부동산 경매 정보 API

## 1. 목적
### API Call Study 및 경매 정보 알람

## 2. 사용 툴

### python을 사용하여 공공 실거래가 API를 이용합니다.
### 아래의 모듈을 import하여야 합니다.
```
  pip install numpy
  pip install tkinter

  python -m pip install mysql-connector
  pip install pymysql
```
### python crawling 사용하는 모듈
```
  pip install selenium
```

### import 모듈
```
  from selenium import webdriver
  import time
  import pymysql as py
```

## 3. 설계 방식

네이버 크롤링을 통하여 대부분의 정보를 가져 옵니다. 
* Selenium  사용법 정리 


```
Void InsertData(Location data)

AuctionData GetRealEstateAuctionData(Location guid)

TradeData GetRealEstateTradeData(Location guid) 

RightValue CalActualValue(Int realTradeVal, Int standardVal,auctionDataType auctionData, tradeDataType tradeData)
```

### 4.번외 코드

크롤링한 데이터를 이용해서 블로그에 데이터를 찍어 주는 프로그램 작성

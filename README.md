# 부동산 경매 정보 API

## 1. 목적
### API Call Study 및 경매 정보 알람

## 2. 사용 툴

### python을 사용하여 공공 실거래가 API를 이용합니다.
### 아래의 모듈을 import하여야 합니다.

'''
pip install numpy
pip install tkinter
'''

## 3. 설계 방식

### InsertData(Location data)

### GetRealEstateAuctionData(Location guid)
-- input : 좌표
-- output : 해당 좌표 경매 데이터들
(경매 데이터 타입 결정 필요)

### GetRealEstateTradeData(Location guid) 
--input : 좌표
--output : 해당 좌표 실거래 데이터들
(실거래 데이터 타입 결정 필요)

### CalActualValue(Int realTradeVal, Int standardVal,auctionDataType auctionData, tradeDataType tradeData)
--input : 실거래가격 , 표준 가격, 경매 데이터, 실거래 데이터
--output : 적정 가격

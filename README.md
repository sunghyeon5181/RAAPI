# 부동산 경매 정보 API

## 1. 목적
### API Call Study 및 경매 정보 알람

## 2. 사용 툴

### Python
### 부동산 실거래가 API

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

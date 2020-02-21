from selenium import webdriver
import time

# def Naver_crawling():

# 크롭 웹 페이지 연경
driver = webdriver.Chrome()
# 시간 딜레이 driver에 주기 예)10초 로딩을 주지만 웹이 2초에 완료된다면 2초후(완료후) 넘어감
driver.implicitly_wait(10)
# 사이트 연결
driver.get('https://land.naver.com/auction/')

# 지역 설정(인천)
area_set = driver.find_element_by_css_selector('#areaBtn28')
area_set.click()
# 물건 종류(전체 보기 버튼 클릭)
sel_all_btn = driver.find_element_by_css_selector('#sel_class_btn1 > a')
sel_all_btn.click()

# 물건 종류(1~55) 1 : 전체
step_2 = driver.find_element_by_css_selector('#sale_type2') # 아파트
step_3 = driver.find_element_by_css_selector('#sale_type3') # 주택
step_4 = driver.find_element_by_css_selector('#sale_type4') # 다가구

step_3.click()
step_4.click()

# 물건 페이지 id코드
page_id = []

# 다음 페이지로 넘어가기 (1,2,3...)
time.sleep(3)
next_Tap = driver.find_element_by_css_selector('#page_navi > div')
next_Tap_last_number = int(next_Tap.text[-1])
for row_1 in next_Tap.text:
    time.sleep(2)
    tbody_tag = driver.find_elements_by_css_selector('#tb > tr')
    print(len(tbody_tag)) # 질문 : 왜 처음에 60개 값이 나오는지 ??
    for row_2 in tbody_tag:
        data_page = row_2.find_element_by_css_selector("td.area > a")
        code = data_page.get_attribute('onclick')
        code_1 = code.split(',')
        code_2 = code_1[1].strip(';)') # type = str
        page_id.append(int(code_2))
    page_id = list(set(page_id)) # 중복제거
    if int(row_1) == next_Tap_last_number:
        pass
    else:
        next_page = driver.find_element_by_css_selector(f'#page_navi > div > a:nth-child({int(row_1)+1})')
        next_page.click()
        print('----')

print(page_id)
print(len(page_id))


# id 코드만 다름
# https://goodauction.land.naver.com/auction/ca_view.php?product_id=1940953&class1=&ju_price1=&ju_price2=&bi_price1=&bi_price2=&num1=&num2=&lawsup=0&lesson=0&next_biddate1=&next_biddate2=&state=91&b_count1=0&b_count2=0&b_area1=&b_area2=&special=0&e_area1=&e_area2=&si=28&gu=0&dong=0&apt_no=0&order=&start=0&total_record_val=&detail_search=&detail_class=&recieveCode=
# https://goodauction.land.naver.com/auction/ca_view.php?product_id=1848387&class1=&ju_price1=&ju_price2=&bi_price1=&bi_price2=&num1=&num2=&lawsup=0&lesson=0&next_biddate1=&next_biddate2=&state=91&b_count1=0&b_count2=0&b_area1=&b_area2=&special=0&e_area1=&e_area2=&si=28&gu=0&dong=0&apt_no=0&order=&start=0&total_record_val=&detail_search=&detail_class=&recieveCode=
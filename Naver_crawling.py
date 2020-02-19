from selenium import webdriver


# def Naver_crawling():

# 크롭 웹 페이지 연경
driver = webdriver.Chrome()
# 시간 딜레이 driver에 주기 예)10초 로딩을 주지만 웹이 2초에 완료된다면 2초후(완료후) 넘어감
driver.implicitly_wait(10)
# 사이트 연결
driver.get('https://goodauction.land.naver.com/auction/ca_list.php')


# 물건 종류(전체 보기 버튼 클릭)
sel_all_btn = driver.find_element_by_css_selector('#sel_class_btn1 > a')
sel_all_btn.click()

# 물건 종류(1~55) 1 : 전체
step_01 = driver.find_element_by_css_selector('#sale_type1')
step_11 = driver.find_element_by_css_selector('#sale_type11')

# id 코드만 다름
# https://goodauction.land.naver.com/auction/ca_view.php?product_id=1940953&class1=&ju_price1=&ju_price2=&bi_price1=&bi_price2=&num1=&num2=&lawsup=0&lesson=0&next_biddate1=&next_biddate2=&state=91&b_count1=0&b_count2=0&b_area1=&b_area2=&special=0&e_area1=&e_area2=&si=28&gu=0&dong=0&apt_no=0&order=&start=0&total_record_val=&detail_search=&detail_class=&recieveCode=
# https://goodauction.land.naver.com/auction/ca_view.php?product_id=1848387&class1=&ju_price1=&ju_price2=&bi_price1=&bi_price2=&num1=&num2=&lawsup=0&lesson=0&next_biddate1=&next_biddate2=&state=91&b_count1=0&b_count2=0&b_area1=&b_area2=&special=0&e_area1=&e_area2=&si=28&gu=0&dong=0&apt_no=0&order=&start=0&total_record_val=&detail_search=&detail_class=&recieveCode=
from selenium import webdriver
import time

def Naver_crawling_id():

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

    # 물건 종류(1~55) 1 : 전체 2:아파트 3:주택
    for i in range(3,5):
        step = driver.find_element_by_css_selector(f'#sale_type{i}')
        step.click()

    # 물건 종류 이름 가져오기
    total_name = []
    kinds_name = driver.find_elements_by_css_selector('#content > div > form > table > tbody > tr:nth-child(1) > td > div > ul > li')
    for i in kinds_name:
        total_name.append(i.text)
    del total_name[0]

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

    return page_id, total_name

def Naver_crawling_data(id_list, kinds_name_list):
    total_data_list = []
    driver = webdriver.Chrome()

    for i in kinds_name_list:
        data_holl = []
        total_data_list.append(data_holl)

    count = 0
    for row_1 in id_list:

        driver.get(f'https://goodauction.land.naver.com/auction/ca_view.php?product_id={row_1}&class1=&ju_price1=&ju_price2=&bi_price1=&bi_price2=&num1=&num2=&lawsup=0&lesson=0&next_biddate1=&next_biddate2=&state=91&b_count1=0&b_count2=0&b_area1=&b_area2=&special=0&e_area1=&e_area2=&si=28&gu=0&dong=0&apt_no=0&order=&start=0&total_record_val=&detail_search=&detail_class=&recieveCode=')

        data_list = []

        time.sleep(2)
        if driver.find_element_by_css_selector('#content2 > div > div.content_wrap > div.content > div:nth-child(4) > table > tbody > tr:nth-child(1) > th').text == "소재지":
            # 소재지 박스
            row_1 = driver.find_element_by_css_selector('#content2 > div > div.content_wrap > div.content > div:nth-child(4) > table > tbody')

            address = row_1.find_element_by_css_selector('tr:nth-child(1) > td > strong')
            data_list.append(address.text)
            kinds_name = row_1.find_element_by_css_selector('tr:nth-child(2) > td:nth-child(2)')
            data_list.append(kinds_name.text)
            building_area = row_1.find_element_by_css_selector('tr:nth-child(3) > td:nth-child(2)')
            data_list.append(building_area.text)
            Land_area = row_1.find_element_by_css_selector('tr:nth-child(4) > td:nth-child(2) > em')
            data_list.append(Land_area.text)


        elif driver.find_element_by_css_selector('#content2 > div > div.content_wrap > div.content > div:nth-child(2) > table > tbody > tr:nth-child(1) > th').text == "소재지":
            row_2 = driver.find_element_by_css_selector('#content2 > div > div.content_wrap > div.content > div:nth-child(2) > table > tbody')

            address = row_2.find_element_by_css_selector('tr:nth-child(1) > td > strong')
            data_list.append(address.text)
            kinds_name = row_2.find_element_by_css_selector('tr:nth-child(2) > td:nth-child(2)')
            data_list.append(kinds_name.text)
            building_area = row_2.find_element_by_css_selector('tr:nth-child(3) > td:nth-child(2)')
            data_list.append(building_area.text)
            Land_area = row_2.find_element_by_css_selector('tr:nth-child(4) > td:nth-child(2) > em')
            data_list.append(Land_area.text)

        else:
            pass
        kinds = data_list[1]
        print(kinds)
        count = count+1
        print(count)
        print('----------')
        kinds_1 = kinds.split('(')
        index = kinds_name_list.index(kinds_1[0])
        total_data_list[index].append(data_list)


    return total_data_list

page_code, total_kinds = Naver_crawling_id()

total = Naver_crawling_data(page_code, total_kinds)
print(total)
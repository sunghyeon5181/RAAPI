from selenium import webdriver
import time

def Naver_crawling_id():

    # 크롭 웹 페이지 연결
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
    for i in range(1,2):
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
    time.sleep(2)
    next_Tap = driver.find_element_by_css_selector('#page_navi > div')

    # "끝"을 체크해서 마지막 번호 가져와 물건 갯수 확인
    if next_Tap.text[-1] == "끝":
        # "끝" 버튼 체크
        page_end = driver.find_element_by_css_selector('#page_navi > div > a.next_end')
        page_end.click()
        time.sleep(2)
        # 마지막 number 가져오기
        last_number_str = driver.find_element_by_css_selector('#page_navi > div > strong')
        last_number_int = int(last_number_str.text)
        # 10개 기준으로 다음 클릭 해야됨 그래서 마지막 number 10으로 나눔
        Daum_click_count = last_number_int // 10

        # 데이터 가져오기 위해서 "처음" 버튼 체크
        page_first = driver.find_element_by_css_selector('#page_navi > div > a.pre_end')
        page_first.click()

    # 10개씩 분류되어 있는 페이지 for문으로 돌림
    for row_1 in range(1,Daum_click_count+2):
        # 1~10페이지(첫번쨰 페이지 "다음"과"끝"이 있는) 물건 확인
        if row_1 == 1:
            # "다음"과 "끝" 삭제
            first_page = driver.find_elements_by_css_selector('#page_navi > div > a')
            next_number_list = []
            for i in first_page:
                next_number_list.append(i.text)
            del next_number_list[-1]
            del next_number_list[-1]
            print(next_number_list)

            # 각 페이지(30개씩 이루어져있는)의 물건 데이터 id코드 가져오기
            for row_2 in range(1,len(next_number_list)+2): # 1~10
                id_code = driver.find_elements_by_css_selector('#tb > tr') # 물건 30개
                # id 가져오기
                for row_3 in id_code:
                    data_tag = row_3.find_element_by_css_selector("td.area > a")
                    code = data_tag.get_attribute('onclick')
                    code_1 = code.split(',')
                    code_2 = code_1[1].strip(';)')  # type = str
                    page_id.append(int(code_2))
                # 1~10 번 까지 한번씩 클릭 하기
                if row_2 == len(next_number_list)+1:
                    pass

                else:
                    next_number = driver.find_element_by_css_selector(f'#page_navi > div.pagnavi > a:nth-child({row_2 +1})')
                    print(row_2+1)
                    print('-------------')
                    next_number.click()
            # "다음" 버튼 클릭하기
            Daum_page = driver.find_element_by_css_selector('#page_navi > div > a.next')
            Daum_page.click()


        # 마지막 페이지 확인(마지막 페이지 "처음","이전" 이존재하는)
        elif row_1 == Daum_click_count+1:
            # "처음","이전" 지우기
            last_page = driver.find_elements_by_css_selector('#page_navi > div > a')
            next_number_list = []
            for i in last_page:
                next_number_list.append(i.text)
            del next_number_list[0]
            del next_number_list[0]
            print(next_number_list)

            # 각 페이지(30개씩 이루어져있는) 물건의 id 가져오기
            for row_2 in range(1,len(next_number_list)+2):
                id_code = driver.find_elements_by_css_selector('#tb > tr')  # 물건 30개
                print(row_2)
                print('------------')
                for row_3 in id_code:
                    data_tag = row_3.find_element_by_css_selector("td.area > a")
                    code = data_tag.get_attribute('onclick')
                    code_1 = code.split(',')
                    code_2 = code_1[1].strip(';)')  # type = str
                    page_id.append(int(code_2))

                # 다음 페이지로 이동(ex 12,13,14,15,16 으로 이루어진 마지막)
                if row_2 == len(next_number_list)+1:
                    pass
                else:
                    # "처음", "이전" 존재함
                    next_number = driver.find_element_by_css_selector(f'#page_navi > div > a:nth-child({row_2 + 3})')
                    next_number.click()


        # 중간("처음"과"이전" 존재 "다음","끝" 존재  )에 이루어져 있는 페이지 입력
        else:
            # "처음","이전","다음","끝"  삭제하기
            middle_page = driver.find_elements_by_css_selector('#page_navi > div > a')
            next_number_list = []
            for i in middle_page:
                next_number_list.append(i.text)
            del next_number_list[0]
            del next_number_list[0]
            del next_number_list[-1]
            del next_number_list[-1]
            print(next_number_list)
            count=0
            # 중간 페이지의 a-tag의 순서가 1~14 까지 있는데 (1,2 : 처음,끝  13,14 : 다음,끝)
            next_number_atag = [4, 5, 6, 7, 8, 9, 10, 11, 12]
            for row_2 in next_number_list :
                id_code = driver.find_elements_by_css_selector('#tb > tr')  # 물건 30개

                for row_3 in id_code:
                    data_tag = row_3.find_element_by_css_selector("td.area > a")
                    code = data_tag.get_attribute('onclick')
                    code_1 = code.split(',')
                    code_2 = code_1[1].strip(';)')  # type = str
                    page_id.append(int(code_2))


                # 다음 number 읽기
                if next_number_atag[count] == 12:
                    pass
                else:
                    next_number = driver.find_element_by_css_selector(f'#page_navi > div > a:nth-child({next_number_atag[count]})')
                    next_number.click()
                    count = count + 1
            # "다음" 클릭하기
            Daum_page = driver.find_element_by_css_selector('#page_navi > div > a.next')
            Daum_page.click()

    page_id = list(set(page_id))
    print(page_id)
    print(len(page_id))
    # data있는 페이지 id,  물건 종료 name(전체, 아파트, 주책, ....)
    return page_id, total_name

def Naver_crawling_data(id_list, kinds_name_list):
    # 전체 데이터 입력 리스트(3차원)
    total_data_list = []
    driver = webdriver.Chrome()

    # 물건 종류 만큼 리스트 생성(아파트 => total_data_list[0] , 주택 => total_data_list[1], .....)
    for i in kinds_name_list:
        data_holl = []
        total_data_list.append(data_holl)

    count_1 = 0
    for row_1 in id_list:

        # id 페이지 들어가기
        driver.get(f'https://goodauction.land.naver.com/auction/ca_view.php?product_id={row_1}&class1=&ju_price1=&ju_price2=&bi_price1=&bi_price2=&num1=&num2=&lawsup=0&lesson=0&next_biddate1=&next_biddate2=&state=91&b_count1=0&b_count2=0&b_area1=&b_area2=&special=0&e_area1=&e_area2=&si=28&gu=0&dong=0&apt_no=0&order=&start=0&total_record_val=&detail_search=&detail_class=&recieveCode=')

        # id 페이지에 데이터 리스트
        data_list = []

        time.sleep(2)

        # 큰 body 태그
        body_tag = driver.find_elements_by_css_selector('#content2 > div > div.content_wrap > div.content > div.section_tbl')
        count_2 = 0
        for row_1 in body_tag:
            count_2 = count_2 + 1
            # class:section_tbl 첫번쨰 테이플
            if count_2 == 1:
                first_tbody = row_1.find_element_by_css_selector('table > tbody')

                # 주소
                address = first_tbody.find_element_by_css_selector('tr:nth-child(1) > td > strong')
                data_list.append(address.text)
                # 물건 종류
                kind = first_tbody.find_element_by_css_selector('tr:nth-child(2) > td:nth-child(2)')
                data_list.append(kind.text)
                # 건물 면적
                building_area = first_tbody.find_element_by_css_selector('tr:nth-child(3) > td:nth-child(2)')
                data_list.append(building_area.text)
                # 대지권
                land_area = first_tbody.find_element_by_css_selector('tr:nth-child(4) > td:nth-child(2) > em')
                data_list.append(land_area.text)

            elif count_2 == 2:
                pass

            elif count_2 == 3:
                pass
            else:
                pass

        # 물건 종류가 위의 물건 종류 name에 있으면 그 리스트 index를 받아서 total 리스트 2차원 공간에 입력(물건종류 순서랑 같게 나열 하고자)
        kinds = kind.text
        print(kinds)
        kinds_1 = kinds.split('(')

        if kinds_1[0] =="다세대":
            index = kinds_name_list.index("빌라등")
            total_data_list[index].append(data_list)
        elif kinds_1[0] =="아파트형공장":
            index = kinds_name_list.index("APT공장")
            total_data_list[index].append(data_list)
        elif kinds_1[0] =="숙박":
            index = kinds_name_list.index("콘도등")
            total_data_list[index].append(data_list)
        else:
            index = kinds_name_list.index(kinds_1[0])
            total_data_list[index].append(data_list)

        count_1 = count_1 + 1
        print(count_1)
        print('-------------')
    return total_data_list

page_code, total_kinds = Naver_crawling_id()
total = Naver_crawling_data(page_code, total_kinds)
print(total)
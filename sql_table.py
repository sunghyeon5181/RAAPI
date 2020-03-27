import Naver_crawling
import pymysql as py

# 크롤링 데이터 import 하기
page_code, total_kinds = Naver_crawling.Naver_crawling_id()
total, total_dict = Naver_crawling.Naver_crawling_data(page_code, total_kinds)

# SQL  연결하기
mydb = py.connect(host="localhost", user="root", password="5181",database="test", charset="utf8")
# cursor 만들기
conn = mydb.cursor()

# for row_1 in total_kinds:
#     conn.execute(f"DROP TABLE {row_1}")


tatel = []
# total_kinds : 물건 종류 리스트
for row_1 in range(0,len(total_kinds)):
    # 각 물건종류의 첫번쨰 물건 가져오기
    tatel_name = total_dict[row_1]
    name = []
    # 딕셔너리 key 값 name 리스트에 입력
    if tatel_name == []:
        name.append("null")
        tatel.append(name)
    else:
        for row_2 in list(tatel_name[0]):
            name.append(row_2)
            # 2차원 리스트로 각 물건종류의 keys 입력
        tatel.append(name)

# table 생성하기
for row_1 in total_kinds:
    count = 0
    # 물건 종류마다 데이터베이스 만들기
    conn.execute(f"CREATE TABLE {row_1}(number VARCHAR(10))")
    for row_2 in range(0,len(tatel[0])):
        # 딕셔너리 key값을 컬럼으로 추가
        conn.execute(f"ALTER TABLE {row_1} ADD {tatel[count][row_2]} VARCHAR(255)")
    count = count + 1


# 데이터 입력



print("종료")






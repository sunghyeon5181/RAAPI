import Naver_crawling
import pymysql as py


class SQL_Table:
    def __init__(self):
        print("테이블 생성")

    def sql_connect(self):
        # SQL  연결하기
        mydb = py.connect(host="localhost", user="root", password="5181",database="test", charset="utf8")
        # cursor 만들기
        conn = mydb.cursor()
        return conn


    def sql_table_DROP(self,conn):
        for row_1 in total_kinds:
            conn.execute(f"DROP TABLE {row_1}")

    def sql_table_CREATE(self,conn,kinds,dict):
        tatel = []
        # total_kinds : 물건 종류 리스트
        for row_1 in range(0,len(kinds)):
            # 각 물건종류의 첫번쨰 물건 가져오기
            column_name = dict[row_1]
            name = []
            # 딕셔너리 key 값 name 리스트에 입력
            if column_name == []:
                name.append("blank")
                tatel.append(name)
            else:
                for row_2 in list(column_name[0]):
                    name.append(row_2)
                    # 2차원 리스트로 각 물건종류의 keys 입력
                tatel.append(name)

        print(tatel)
        print('--------------------')
        print(kinds)

        # table 생성하기
        count = 0
        for raw_1 in kinds:
            # 물건 종류마다 데이터베이스 만들기
            conn.execute(f"CREATE TABLE {raw_1}(number VARCHAR(10))")
            for raw_2 in range(0,len(tatel[count])):
                # 딕셔너리 key값을 컬럼으로 추가
                conn.execute(f"ALTER TABLE {raw_1} ADD {tatel[count][raw_2]} VARCHAR(255)")
            count = count + 1

    def sql_table_UPDATA(self):
        print("미완성")
        #데이터 입력





# 크롤링 데이터 import 하기
Nc = Naver_crawling.Naver()
page_code, total_kinds = Nc.Naver_crawling_id()
total_list, total_dict = Nc.Naver_crawling_data(page_code, total_kinds)

#SQL 테이블 생성
St = SQL_Table()
con = St.sql_connect()
St.sql_table_CREATE(con,total_kinds,total_dict)

print("종료")






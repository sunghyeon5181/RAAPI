import Naver_crawling
import pymysql as py


class SQL_Table:
    def __init__(self):
        print("프로그램 시작")

        print("크롤링 시작")
        # 크롤링 데이터 import 하기
        Nc = Naver_crawling.Naver()
        page_code, total_kinds = Nc.Naver_crawling_id()
        total_list, total_dict = Nc.Naver_crawling_data(page_code, total_kinds)

        print("테이블 생성")

        # SQL 테이블 생성

        conn_body, mydb_body = self.sql_connect()
        self.sql_table_DROP(conn_body, total_kinds)
        column_kins = self.sql_table_CREATE(conn_body, total_kinds, total_dict)
        self.sql_table_UPDATA(conn_body, total_kinds, total_list, column_kins)
        mydb_body.commit()

        print("종료")

    def sql_connect(self):
        # SQL  연결하기
        mydb = py.connect(host="localhost", user="root", password="5181", database="test", charset="utf8")
        # cursor 만들기
        conn = mydb.cursor()
        return conn, mydb


    def sql_table_DROP(self,conn,kinds):
        for row_1 in kinds:
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


        # table 생성하기
        count = 0
        for raw_1 in kinds:
            # 물건 종류마다 데이터베이스 만들기
            conn.execute(f"CREATE TABLE {raw_1}(number VARCHAR(10))")
            for raw_2 in range(0,len(tatel[count])):
                # 딕셔너리 key값을 컬럼으로 추가
                conn.execute(f"ALTER TABLE {raw_1} ADD {tatel[count][raw_2]} VARCHAR(255)")
            count = count + 1

        return tatel

    def sql_table_UPDATA(self,conn,kinds,list,column_zero):

        count_1 = 0
        # table 이름 사용
        for row_1 in kinds:
            count_2 = 0
            # 물건이 없는 경우
            if list[count_1] == []:
                conn.execute(f"INSERT INTO {row_1} (number) VALUE ({count_2+1})")
                count_1 = count_1 + 1
            else:
                # 물건이 존재 하는경우
                for row_2 in list[count_1]:
                    # number 컬럼 순서 입력
                    row_2.insert(0,str(count_2+1))
                    del row_2[14]
                    # 컬럼과 list 갯수 맞추기

                    if len(row_2) == len(column_zero[count_1])+1:
                        conn.execute(f"INSERT INTO {row_1} VALUES {tuple(row_2)} ")
                        count_2 = count_2 + 1
                    else:
                        list_add_blank = (len(column_zero[count_1])+1) - len(row_2)
                        for row_3 in range(0,list_add_blank):
                            row_2.append(" ")
                        conn.execute(f"INSERT INTO {row_1} VALUES {tuple(row_2)} ")
                        count_2 = count_2 + 1
                count_1 = count_1 + 1
                # count_1 : list 순서 / count_2 : list 안에 값들 순서

# class 시작
SQL_Table()




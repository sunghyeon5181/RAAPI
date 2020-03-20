# import Naver_crawling
from selenium import webdriver
import time

import pymysql as py



# page_code, total_kinds = Naver_crawling.Naver_crawling_id()
# total, total_dict = Naver_crawling.Naver_crawling_data(page_code, total_kinds)

mydb = py.connect(host="localhost", user="root", password="5181",database="test", charset="utf8")

conn = mydb.cursor()
conn.execute("CREATE TABLE test1 (kinds VARCHAR(100), address VARCHAR(255), number VARCHAR(30))")
conn.execute("SHOW TABLES")

for i in conn:
    print(i)


    
conn.execute("DROP TABLE test1")


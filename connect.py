import pymysql
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='stockmanagementsystem'
    )
    return conn

conn = connection()
cursor = conn.cursor()
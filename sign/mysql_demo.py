from pymysql import cursors, connect

conn = connect(host='127.0.0.1', user='root', password='liu#123456', db='guest', charset='utf8mb4', cursorclass=cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        sql = 'INSERT INTO sign_guest (realname,phone,email,sign,event_id, \
              create_time) VALUES \
            ("tom",18825678958,"tom@mail.com",0,1,NOW()); '
        cursor.execute(sql)
        conn.commit()
        with conn.cursor() as currsor:
            sql ="select realname,phone,email,sign FROM sign_guest where phone=%s"
            cursor.execute(sql,('18825678958',))
            result = cursor.fetchone()
            print(result)
finally:
    conn.close()

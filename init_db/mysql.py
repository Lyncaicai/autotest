# coding=utf-8
from pymysql import connect, cursors


class MySql:
    def __init__(self, host, port, user, password, dbname):
        try:
            self.conn = connect(
                host=host,
                port=port,
                user=user,
                password=password,
                db=dbname,
                charset='utf8mb4',
                cursorclass=cursors.DictCursor
            )
        except Exception as e:
            print(e)

    def excute_sql(self, sql):
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    bms = MySql('192.168.0.32', 3306, 'ceshi', 'ceshi', 'gmf_bms')
    sql = 'delete from product_group where org_id="23"'
    bms.excute_sql(sql)
    bms.close()

# coding=utf-8
from mysql import MySql


def init_fund():
    bms = MySql('192.168.0.32', 3306, 'ceshi', 'ceshi', 'gmf_bms')
    sql = 'delete from product_group where org_id="23"'
    bms.excute_sql(sql)
    bms.close()

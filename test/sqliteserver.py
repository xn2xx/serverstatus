#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : hsx
import sqlite3

"""
数据库操作
"""


class SqliteServer:

    @staticmethod
    def __sql_operation(sql):
        conn = sqlite3.connect("../sqlite/serverstatus.db")
        curses = conn.cursor()
        curses.execute(sql)
        conn.commit()
        return curses.fetchall()

    @staticmethod
    def query_info():
        sql = "select * from server_info"
        result = SqliteServer.__sql_operation(sql)
        if not result:
            return print("没有此ip")
        else:
            return result

    @staticmethod
    def query_ipaddr_info(ipaddr=None):
        sql = "select s.ipaddr,s.username,s.password,s.terminal,s.port,s.protocol from server_info s where s.ipaddr = '{}'".format(
            ipaddr)
        result = SqliteServer.__sql_operation(sql)
        if not result:
            return print("没有此ip")
        else:
            return result


# if __name__ == '__main__':
#     sqls = SqliteServer
# for i in sqls.select_ipaddr_info('demo.scitqn.cn'):
#     print(i)

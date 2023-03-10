#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : hsx
import logging
import sqlite3

"""
数据库操作
"""


class SqliteServer:
    def __init__(self, ipaddr=None, username=None, password=None, terminal=None, port=None, protocol=None):
        self.ipaddr = ipaddr
        self.username = username
        self.password = password
        self.terminal = terminal
        self.port = port
        self.protocol = protocol

    @staticmethod
    def __sql_operation(sql):
        """sqlite连接方法"""
        conn = sqlite3.connect("../sqlite/serverstatus.db")
        conn.row_factory = SqliteServer.dict_factory
        curses = conn.cursor()
        curses.execute(sql)
        desc = curses.fetchall()
        conn.commit()
        # for row in desc:
        #     return row
        return desc

    @staticmethod
    def query_info():
        """查询数据库所有连接信息"""
        sql = "select * from server_info"
        result = SqliteServer.__sql_operation(sql)
        if not result:
            return "数据库没有数据"
            logging.WARN("数据库没有数据")
        else:
            return result

    @staticmethod
    def query_ipaddr_info(ipaddr=None):
        """通过ip查询数据库的服务器连接信息"""
        sql = "select s.ipaddr,s.username,s.password,s.terminal,s.port,s.protocol from server_info s where s.ipaddr = " \
              "'{}'".format(
            ipaddr)
        result = SqliteServer.__sql_operation(sql)
        if not result:
            # logging.WARN("没有此ip")
            return "沒有此ip"
        else:
            return result

    @staticmethod
    def dict_factory(cursor, row):
        """数据返回成为字典格式"""
        d = {}
        for index, col in enumerate(cursor.description):
            d[col[0]] = row[index]
        return d


if __name__ == '__main__':
    res: dict = SqliteServer.query_info()
    print(res)
    # res: dict = SqliteServer.query_ipaddr_info("demo1.scitqn.cn")

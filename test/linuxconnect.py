#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : hsx
import re
import sqliteserver
import ssh_executor


class LinuxConnect:
    def __init__(self, in_ipaddr, execmd):
        sqls = sqliteserver.SqliteServer.query_ipaddr_info(in_ipaddr)
        if isinstance(sqls, list):
            for res in sqls:
                self.ipaddr = res.get('ipaddr')
                self.username = res.get('username')
                self.password = res.get('password')
                self.port = res.get('port')
                self.execmd = execmd

    def connect_linux(self):
        """连接Linux并且发送命令，接收命令返回值"""

        executor = ssh_executor.SSHExecutor(ipaddr=self.ipaddr, port=self.port, username=self.username,
                                            password=self.password, cmd_str=self.execmd).get_connect()
        return executor

    @staticmethod
    def linux_pid(cmd):
        """获取Linux服务pid"""
        # 截掉用户
        if cmd != "":
            num1 = re.search(r'\s', cmd).start()
            str1 = cmd[num1:]
            # 截掉空格
            num2 = re.search(r'\d', str1).start()
            str2 = str1[num2:]
            # 截出PID
            num3 = re.search(r'\s', str2).start()
            pid = str2[:num3]

            cmd = 'kill ' + pid
            print(cmd)
            return cmd
        else:
            print("无此进程")


if __name__ == '__main__':
    lsx = LinuxConnect(in_ipaddr='192.168.2.26', execmd='fast')
    ret_cmd = ""
    print(lsx.connect_linux())

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : hsx
import paramiko
import sqliteserver


class LinuxConnect:

    @staticmethod
    def connect_linux(ipaddr=None, port=None, username=None, password=None, execmd=None):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ipaddr, port=port, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(execmd)
        stdin.write("Y")
        print(stdout.read().decode('utf-8'))
        ssh.close()

    # @staticmethod
    # def query_pid():


if __name__ == '__main__':
    sqls = sqliteserver.SqliteServer
    result = sqls.query_ipaddr_info('demo.scitqn.cn')
    for info in result:
        ipaddr = info[0]
        port = info[4]
        username = info[1]
        password = info[2]
        execmd = "free -h"

    LinuxConnect.connect_linux(ipaddr, port, username, password, execmd)

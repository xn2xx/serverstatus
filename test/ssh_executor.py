#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/8/7 17:49
# @Author : hsx
# @File : ssh_executer
import paramiko
from paramiko.ssh_exception import AuthenticationException, NoValidConnectionsError


class SSHExecutor:
    def __init__(self, ipaddr, port, password, username, cmd_str):
        self.ipaddr = ipaddr
        self.port = port
        self.password = password
        self.username = username
        self.cmd_str = cmd_str

    def get_connect(self):
        """创建Linux连接"""
        ssh = paramiko.SSHClient()  # 创建连接
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(hostname=self.ipaddr, port=self.port, username=self.username, password=self.password,
                        timeout=1000)
        except TimeoutError:
            return "连接超时"
        except NoValidConnectionsError as e:
            return "连接失败"
        except AuthenticationException as e:
            return "用户名或密码错误"
        else:
            stdin, stdout, stderr = ssh.exec_command(self.cmd_str)  # 发送命令
            out = to_str(stdout.read())     # 正确输出
            err = to_str(stderr.read())     # 错误输出
            if out == "":
                return err
            else:
                return out
        finally:
            ssh.close()


def to_str(bytes_or_str):
    """输出信息转为utf-8"""
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value


if __name__ == '__main__':
    con = SSHExecutor(ipaddr='192.168.2.26', port=22, username='root', password='123456', cmd_str='ping -c 5 www.baidu.com')
    print(con.get_connect())

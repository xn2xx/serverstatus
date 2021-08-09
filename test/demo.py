import paramiko
from setuptools import unicode_utils


def connect():
    global ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


connect()
ssh.connect(hostname='192.168.2.26', port=22, username='root', password='123456', timeout=2000)
stdin, stdout, stderr = ssh.exec_command('df -h')
print(stdout.read().decode('utf-8'))
ssh.close()

unicode_utils
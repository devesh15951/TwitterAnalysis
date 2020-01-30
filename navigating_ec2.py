# -*- coding: utf-8 -*-
"""
Created on Wednesday Jan 29 22:25:16 2020
@author: Devesh Waingankar
Python Version: 3.6 or above
"""
import paramiko

key = paramiko.RSAKey.from_private_key_file(r'path\of\your\pemkey\file.pem')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance
try:
    # Here 'ec2-user' is user name and 'hostname' is public IP of EC2
    client.connect(hostname="X.X.X.X", username="ec2-user", pkey=key)

    # Execute a command stdin.write in an order, after connecting/ssh to the instance
    channel = client.invoke_shell()
    stdin = channel.makefile('wb')
    stdout = channel.makefile('rb')

    stdin.write('''
    command1
    command2
    command3
    exit
    ''')

    client.close()


except Exception as e:
    print (e)

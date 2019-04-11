# -*- coding:utf-8 -*-
# py 2.7.14
import socket


def valid(str):
    clean = ' '.join(str.split())
    for i in range(1, len(clean)):
        if clean[i] == ' ':
            if clean[i - 1].isdigit() and clean[i + 1].isdigit():
                return 0
    return 1


def check_input(string):
    string = string.replace(' ', '')
    # print 'error'
    return string


ip_addr = '172.     1 68.5.1'

# print ' '.join(ip_addr.split())

if not valid(ip_addr):
    print 'error!'
else:
    ip_addr = check_input(ip_addr)
    # packed_ip_addr = socket.inet_aton(ip_addr)

    packed_ip_addr = int(socket.inet_aton(ip_addr).encode('hex'), 16)  # inet_aton转换

    print packed_ip_addr

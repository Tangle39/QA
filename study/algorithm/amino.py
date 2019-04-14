# -*- coding:utf-8 -*-
# py 2.7.14,author = Tangle'
'''
Programming Question:
Convert an IPv4 address in the format of null-terminated C string into a 32-bit integer.
For example, given an IP address “172.168.5.1”, the output should be a 32-bit integer with “172” as the highest order 8 bit,
168 as the second highest order 8 bit, 5 as the second lowest order 8 bit, and 1 as the lowest order 8 bit. That is,
"172.168.5.1" => 2896692481 Requirements:
1. You can only iterate the string once.
2. You should handle spaces correctly: a string with spaces between a digit and a dot is a valid input; while a string with spaces between two digits is not.
"172[Space].[Space]168.5.1" is a valid input. Should process the output normally.
"1[Space]72.168.5.1" is not a valid input. Should report an error. 3. Please provide unit tests.
'''
import socket


def valid(str):
    if not str: return 0
    clean = ' '.join(str.split())
    for i in range(1, len(clean)):
        if clean[i] == ' ':
            if clean[i - 1].isdigit() and clean[i + 1].isdigit():
                return 0
    return 1


def check_input(string):
    string = string.replace(' ', '')

    return string


def conver_ip(ip_addr):
    if not valid(ip_addr):
        return 'error!'
    else:
        ip_addr = check_input(ip_addr)

    packed_ip_addr = int(socket.inet_aton(ip_addr).encode('hex'), 16)  # this function can easily convert

    return packed_ip_addr

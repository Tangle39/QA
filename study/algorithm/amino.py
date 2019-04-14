# py 2.7.14,author = Tangle'
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

    packed_ip_addr = int(socket.inet_aton(ip_addr).encode('hex'), 16)

    return packed_ip_addr

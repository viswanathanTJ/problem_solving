import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Socket created')

ip = socket.gethostbyname('www.viswa2k.tk')

s.connect((ip, 5000))

print('Socket connected to viswa2k')
# # 
# #import regular expressions library
# import re

# #file handler variable
# fh = open("1.txt")

# #initial variable is 0
# y = 0

# #for each x inside regex, find all values that has 1 or more [0-9] characters, using fh variable.read()
# for x in re.findall('[0-9]+',fh.read()):
    
#     #turn x into integer since the output was initially a string, then add it to previous value
#     y = int(x) + y

# #print the value
# print(y)
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('1.txt', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
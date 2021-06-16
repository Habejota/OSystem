from os import system, chdir
from time import sleep
from random import randint
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = randint(500, 65535)
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)

print(fr'Host: {host}')
print(fr'PORT: {port}')
addr = (host, port) 
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serv_socket.bind(addr) 
serv_socket.listen(10) 
print("Waiting graphical connection!")
con, cliente = serv_socket.accept() 
print("Connecting. . .") 
print("Waiting a mensage. . .")
while True:
    try:
        recebe = con.recv(1024) 
        print(recebe.decode())
    except KeyboardInterrupt:
        break
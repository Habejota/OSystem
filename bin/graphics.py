from os import system, chdir
from time import sleep
from random import randint
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = randint(500, 65535)
hostname = socket.gethostname()
host = socket.gethostbyname(hostname)

print(fr'Informations for connect!')
print(fr'Host: {host}')
print(fr'PORT: {port}')
print(fr'Corrent Key: {randint(100, 1000)}')
addr = (host, port) 
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serv_socket.bind(addr) 
serv_socket.listen(10) 
print("Waiting graphical OSystem connection!")
con, adress = serv_socket.accept()
system("cls") 
print("Connecting. . .") 
print("Waiting a mensage. . .")
while True:
    try:
        recebe = con.recv(1024) 
        if recebe.decode() == "sendfile":
            namefile = con.recv(1024)
            print("=" * 70)
            while True:
                filetext = con.recv(1024)
                if filetext.decode() == ":::>>>stop<<<:::":
                    break
                else:
                    print(filetext.decode())
            print("=" * 70)
        else:
            print("User Mensage: ", recebe.decode())
    except KeyboardInterrupt:
        break
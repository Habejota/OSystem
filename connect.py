from os import system, chdir
from time import sleep
from random import randint
import socket
from threading import Thread

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = str(input("Host: "))
try:
    port = int(input("Port: "))
except:
    print("PORT must be a number!")

def client():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.connect((host, port))
            connectadospraku = True
            break
        except KeyboardInterrupt:
            connectadospraku = False
            break
        except:
            print(fr"Fail to Connect with {host}:{port}")
    if connectadospraku == True:
        while True:
            try:
                msg = input("User Mensage: ").encode()
                s.sendall(msg)
            except KeyboardInterrupt:
                s.close()  
                break
    else:
        print("You arent connected to server!")
client()
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
            connectadospraku = False
            break
    if connectadospraku == True:
        while True:
            try:
                msg = input("User Mensage: ")
                if msg == "sendfile":
                    s.sendall(msg.encode())
                    namefile = input("Filename: ")
                    s.sendall(namefile.encode())
                    try:
                        with open(namefile, 'rb') as file:
                            for data in file.readlines():
                                s.sendall(data)
                        print("File text sended!")
                    except:
                        print("This file not founded in system!")
                else:
                    s.sendall(msg.encode())
            except KeyboardInterrupt:
                s.close()  
                break
    else:
        print("You arent connected to server!")
client()
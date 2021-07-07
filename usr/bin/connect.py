from os import system, chdir, getcwd, startfile
from time import sleep as wait
from random import randint as randomic
import socket, sys
from getpass import getpass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Putty:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.host = socket.gethostbyname(self.hostname)

        self.getInformationToConnect()
        self.Secure_SHell()

    def getInformationToConnect(self):
        self.host_connect = str(input("Please, Insert a host to connect: "))
        self.port_connect = int(input('Please, Insert a port to connect to "{}": '.format(self.host_connect)))
    def Secure_SHell(self):
        try:
            s.connect((self.host_connect, self.port_connect))
        except:
            print("Fail to connect to {}:{}".format(self.host_connect, self.port_connect)) 
        else:     
            system("cls")
            self.user = str(input("login as: "))
            self.password = getpass(f"{self.user}@{self.host_connect}'s password: ").strip()
            while True:
                try:
                    cmd = input(">>> ").strip().lower()
                    if cmd == "exit":
                        print("Closing Internal connection. . ."), wait(3.834)
                        s.close()
                        break
                    elif cmd == "passwd":
                        self.umhfnyv = getpass("Old Password: ")
                        if self.umhfnyv == self.password:
                            self.password = getpass("New Password: ").strip()
                            passwdcu = getpass("Repeat new password: ").strip()
                            if self.password == passwdcu:
                                print("Password was charged with sucessfuly!")
                    elif cmd.startswith("echo"):
                        cmd = cmd.replace("echo")
                        s.send(cmd.encode())
                        print("The mensage was sended to server!")


                    else:
                        print("SSH: {}: Unknow CommandError!".format(cmd))
                except KeyboardInterrupt:
                    print("")
                except Exception as e:
                    print(e)
                    break

Putty()
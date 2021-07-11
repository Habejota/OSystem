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
                    cmd = input(rf"{self.user}@{self.host_connect}:/network# ").strip().lower()
                    if cmd == "exit":
                        print("Closing Internal connection. . ."), wait(3.834)
                        s.close()
                        print("[  OK  ] Closed Connection With Sucess!")
                        break
                    elif cmd.startswith("passwd"):
                        if cmd == "passwd":
                            self.umhfnyv = getpass("Old Password: ")
                            if self.umhfnyv == self.password:
                                self.password = getpass("New Password: ").strip()
                                passwdcu = getpass("Repeat new password: ").strip()
                                if self.password == passwdcu:
                                    print("Password was charged with sucessfuly!")
                        elif cmd == "passwd -s":
                            print("USERNAME={}".format(self.user))
                            print("HOST={}".format(self.host))
                            print("PASSWORD_ROOT={}".format(self.password))
                        else:
                            print("SSH: passwd [arguments] (parameters)")
                            print("  passwd - Charge Host Password")
                            print("  -s - Show setup Hosted")
                    elif cmd.startswith("nano"):
                        cmd = cmd.replace("nano", "")
                        cmd = cmd.replace("nano ", "")
                        system("nano {}".format(cmd))
                    elif cmd.startswith("sendfile"):
                        cmd = cmd.replace("sendfile ", "")
                        cmd = cmd.replace("sendfile", "")  
                        try:
                            a = open(cmd)
                        except FileNotFoundError:
                            print("[FAILED] FileNotFoundError!")
                        except Exception as ex:
                            print("[FAILED] {}".format(ex))
                        else:
                            with open(cmd, "rt") as fileText:
                                s.sendfile(fileText.read())
                            print("[  OK  ] File Sended with sucessfuly!")
                    elif cmd.startswith("login"):
                        if cmd == "login start":
                            try:
                                a = open(".socket", "rt")
                            except FileNotFoundError:
                                print("[FAILED] Cannot open history log file.")
                                spd = open(".socket", "wt+")
                                print("[  OK  ] All right in System registration.")
                                print("[  OK  ] SSH loged to Addon Resource File.")
                            else:
                                spd = open(".socket", "wt")
                                print("[  OK  ] All right in System registration.")
                                print("[  OK  ] SSH loged to Addon Resource File.")
                        elif cmd == "login stop":
                            try:
                                spd.close()
                            except:
                                print("[FAILED] Sorry: May you start a connection first!")
                            else:
                                print("[  OK  ] SSH: The connection was closed with Sources.")
                            
                        else:
                            print("SSH: login: Specific the argument")
                            print(" start - Start a connection with Resource Packs")
                            print(" stop - Stop the connection with Packs")
                    
                    elif cmd.startswith("echo"):
                        cmd = cmd.replace("echo", "")
                        try:
                            spd.write(cmd)
                        except:
                            print("[FAILED] Cannot Read the Resources Packages")
                        else:
                            s.send(cmd.encode())
                            print("[  OK  ] The mensage was sended to server!")
                    elif cmd == "clear":
                        system("cls")
                    elif cmd == "pwd":
                        print(getcwd())
                    elif cmd == "sended":
                        try:
                            with open(".socket", "rt") as socketFile:
                                print(socketFile.read())
                        except FileNotFoundError:
                            print("[FAILED] You dont have installed any Package!")
                    

                    else:
                        print("SSH: {}: Unknow CommandError!".format(cmd))
                except KeyboardInterrupt:
                    print("")
                except Exception as e:
                    print("[FAILED] {}".format(e))
                    break

Putty()

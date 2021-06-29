# Importing Python modules
from os import chdir, system
from time import sleep
from socket import gethostname, gethostbyname

# Firmware definition
hostname = gethostname()
ifconfig = gethostbyname(hostname)

# Firmware Main Classes
class Firmware:
    def __init__(self):
        self.FirmwareConsole()
        
    def FirmwareConsole(self):
        system("title Advanced Firmware")
        system("cls")
        
        while True:
            try:
                cmd: str = input("iPXE> ").strip()
                if cmd == "ifstat":
                    print("net0: 52:54:00:12:34:56 using rtl8139 on PCI00:03.0 (Ethernet) [closed]\n[Link:up, TX:0 TXE:0 RX:0 RXE:0]")
                elif cmd == "route":
                    print("net0: 10.0.0.155/255.255.255.0 gw 10.0.0.1")
                elif cmd == "exit":
                    break
                elif cmd == "ifconfig":
                    print(rf"""Software Loopback Interface 1
    Link encap: Local loopback
    inet addr:{ifconfig} Mask: 255.0.0.0
    MTU: 1500 Speed:1073,74 Mbps
    Admin status:UP Oper status:OPERATIONAL
    RX packets:0 dropped:0 errors:0 unkown:0
    TX packets:0 dropped:0 errors:0 txqueuelen:0

Qualcomm Atheros QCA9377 Wireless Network Adapter
    Link encap: IEEE 802.11 HWaddr: 5C-C9-D3-8D-23-9E
    inet addr:{ifconfig} Mask: 255.255.255.0
    MTU: 1500 Speed:108,30 Mbps
    Admin status:UP Oper status:OPERATIONAL
    RX packets:154204 dropped:0 errors:0 unkown:0
    TX packets:106105 dropped:0 errors:0 txqueuelen:0""")
                elif cmd == "hostname":
                    print(hostname)
                else:
                    print("iPXE: {}: Unknow Command!".format(cmd))
                
                
                
            except KeyboardInterrupt:
                input("\n\nPress ENTER to turn off the computer. . .")
                break
            
                
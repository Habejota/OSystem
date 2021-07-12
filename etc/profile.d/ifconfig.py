from socket import gethostname, gethostbyname
a = gethostname()
ifconfig = gethostbyname(a)
print(rf"""Software Loopback Interface 1
    Link encap: Local loopback
    inet addr:{ifconfig} Mask: 255.0.0.0
    MTU: 1500 Speed:1073,74 Mbps
    Admin status:UP Oper status:OPERATIONAL
    RX packets:0 dropped:0 errors:0 unkown:0
    TX packets:0 dropped:0 errors:0 txqueuelen:0

Qualcomm Atheros QCA9377 Wireless Network Adapter
    Link encap: IEEE 802.11 HWaddr: 5C-C9-D3-8D-23-9D
    inet addr:{ifconfig} Mask: 255.255.255.0
    MTU: 1500 Speed:108,30 Mbps
    Admin status:UP Oper status:OPERATIONAL
    RX packets:154204 dropped:0 errors:0 unkown:0
    TX packets:106105 dropped:0 errors:0 txqueuelen:0""")
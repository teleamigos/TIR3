from Flooding import *
from socket import socket, AF_PACKET, SOCK_RAW, htons

"""-----------------------------------------------------------------------------
---------------------------This is main file------------------------------------
-----------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------
----------------------------Init section-------------------------------------"""
F=Flooding()
s=socket(AF_PACKET,SOCK_RAW,htons(0x0800))
s.bind(("wlp1s0",0))
"""-----------------------------------------------------------------------------
----------------------------User section-------------------------------------"""
print("You are user A, your direction is : ", F.user['A'])
user =input("Type the user you want send a message(B,C or D) : ")
message=input(f"Type a message for user {user} : ")
F.create_payload(0,message)
msj_out=F.create_package(F.user['A'],F.user['D'])
"""-----------------------------------------------------------------------------
---------------------------send information----------------------------------"""

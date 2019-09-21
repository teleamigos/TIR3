from Flooding import *
#from socket import socket, AF_PACKET, SOCK_RAW, htons

"""-----------------------------------------------------------------------------
---------------------------This is main file------------------------------------
-----------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------
----------------------------Init section-------------------------------------"""
F=Flooding('A')
#s=socket(AF_PACKET,SOCK_RAW,htons(0x0800))
#s.bind(("wlp1s0",0))
"""-----------------------------------------------------------------------------
----------------------------User section-------------------------------------"""
print("You are user A, your direction is : ", F.user['A'])
op=input("Type Y fo send a message : ")
if op=="Y":
    """ getting information """
    user =input("Type the user you want send a message(B,C or D) : ")
    message=input("Type a message for user {user} :")
    F.create_payload(0,message)
    msj_out=F.create_package('A','D')
    """-------------------------------------------------------------------------
    ------------------------send information---------------------------------"""
else :
    """Listening for somenthin...."""
    pass

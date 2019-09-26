"""-----------------------------------------------------------------------------
---------------------------This is main file------------------------------------
-----------------------------------------------------------------------------"""
from socket import socket, AF_PACKET, SOCK_RAW, htons
from Flooding import*
from Threaded_send import*
import time
from threading import Thread

"""-----------------------------------------------------------------------------
----------------------------Init section-------------------------------------"""
usr_name=input("Type your user name : ")
F=Flooding(usr_name)
s=socket(AF_PACKET,SOCK_RAW,htons(0x0801))
#s.bind(("wlp1s0",0))
print("Your user ID   : ",F.my_ID)
c=0
ID=0
"""-----------------------------------------------------------------------------
--------------------------------User-----------------------------------------"""
op=input('Enter "Y" to send a message : ')
while True:
    if op=='Y':
        if F.sequence==0:
            """First message"""
            start=time.time()
            thread2=Thread(target=Type_info_new,args=(F,s))
            thread2.start()
            thread2.join()
        elif ID==F.my_ID:
            """This is not a first message"""
            start=time.time()
            thread3=Thread(target=Type_info_reply,args=(F,s,dst_add))
            thread3.start()
            thread3.join()
    print("Listening : ")
    #msj=s.recv(1024)
    """if not msj:
        print("Not infomation received.")
        break"""
    """mensaje de preuba"""
    
    if Iscorrect(msj) != '1':
        print("Desempaquetando : ")

    elif Iscorrect(msj) !='0':
        print('reenviado')

    else :
        print("Descartado")

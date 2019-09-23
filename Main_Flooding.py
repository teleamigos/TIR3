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
s.bind(("wlp1s0",0))

"""-----------------------------------------------------------------------------
--------------------------------User-----------------------------------------"""
op=input("Type Y/N to send a message ")
while True:
    if op=='Y':
        dst_user=input("Type the user you want to send something : " )
        message=input("Type a message you want to send to {} :".format(dst_user))
        F.create_payload(0,message,dst_user)
        msj_out=F.create_package(usr_name)
        #Abrimos nuevo hilo para enviar
        start=time.time()
        thread1=Thread(target=threaded_send,args=(msj_out,s))
        thread1.start()
        print("------------")
        thread1.join()

    msj=s.recv(1024)
    if not msj:
        print("Not infomation...")
        break
    if F.Unpack_message(msj)!='0':
        msj_rcved=F.Unpack_message(msj)
        print("Message received from {} :".format(F.src_add),msj_rcved)
        op=input("Do you want to reply ? Y/N :")
    else :
        #Abrimos nuevo hilo para retransmitir
        thread1.start()
        print("------------")
        #thread1.join()

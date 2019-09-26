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
print("Your user ID   : ",F.my_ID)
c=0
ID=0
"""-----------------------------------------------------------------------------
--------------------------------User-----------------------------------------"""
print("Connection established.")
op=input('Enter "Y" to send a message : ')
while True:
    if op=='Y':
        if F.sequence==0:
            """First message"""
            start=time.time()
            thread2=Thread(target=Type_info_new,args=(F,s))
            thread2.start()
            #thread2.join()
        elif ID==F.my_ID:
            """This is not a first message"""
            start=time.time()
            thread3=Thread(target=Type_info_reply,args=(F,s,dst_add))
            thread3.start()
            thread3.join()
    print("Listening : ")
    #msj=s.recv(1024)
    if not msj:
        print("Not infomation received.")
        break
    if F.Iscorrect(msj)!='0':
        """Unpack de message"""
        if F.IsRepeated(msj)=='1':
            ID,message,dst_add=F.Unpack_message(msj)
            print('Message received from ID : {}'.format(ID),message)
            """for u in F.user:
                if F.user[u]==ID:
                    dst_user=u"""
            op=input('Type "Y" to reply to the user : ')

            F.sequence +=1
            if op !='Y':
                F.sequence=0
                ID=0
                #op='Y'
        else:
            print("Message was discarded...")
            #F.message_h=[]

    else :
        """Retransmitting"""
        L=len(msj)
        payload=msj[14:L-4]
        new_message=F.retransmitting(msj,payload)
        print("message is retransmitted...",new_message)
        """start=time.time()
        thread1=Thread(target=threaded_send,args=(new_message,s))
        thread1.start()
        thread1.join()"""
        op='N'
        last_msj=msj
        F.sequence=0

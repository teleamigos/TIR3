"""-----------------------------------------------------------------------------
---------------------------This is main file------------------------------------
-----------------------------------------------------------------------------"""
#from socket import socket, AF_PACKET, SOCK_RAW, htons
from Flooding import*
from Threaded_send import*
import time
from threading import Thread

"""-----------------------------------------------------------------------------
----------------------------Init section-------------------------------------"""
usr_name=input("Type your user name : ")
F=Flooding(usr_name)
#s=socket(AF_PACKET,SOCK_RAW,htons(0x0801))
#s.bind(("wlp1s0",0))
print("Your user ID   : ",F.my_ID)
c=0
"""-----------------------------------------------------------------------------
--------------------------------User-----------------------------------------"""
op=input('Enter "Y" to send a message : ')
while True:
    if op=='Y':
        if F.sequence==0:
            """First message"""
            dst_user=input("Type the user you want to send something (A,B,C or D) : " )
            message=input("Type a message you want to send to {} with ID {} :".format(dst_user,F.user[dst_user]))
            payload=F.create_payload(dst_user,message)
            print("payload : ",payload)
            msj_out=F.create_package(F.broadcast,F.my_add,payload)
            print("Message to ID {}  and sequence {} to send  : ".format(F.user[dst_user],F.sequence),msj_out)
            #start=time.time()
            #thread1=Thread(target=threaded_send,args=(msj_out,s))
            #thread1.start()
            #print("------------")
            #thread1.join()
        else :
            """This is not a first message"""
            message=input("Type a message you want to send to {} with ID {} :".format(dst_user,F.user[dst_user]))

    #msj=s.recv(1024)
    """    if not msj:
            print("Not infomation...")
            break"""
    if F.Unpack_message(msj_out)!='0':
        """Unpack de message"""
        ID,message=F.Unpack_message(msj_out)
        print('Message received from ID : {}'.format(ID),message)
        for u in F.user:
            if F.user[u]==ID:
                dst_user=u
        op=input('Type "Y" to reply to the user {}'.format(dst_user) )
        F.sequence +=1

    else :
        """Retransmitting"""
        L=len(msj_out)
        payload=msj_out[14:L-4]
        new_message=F.retransmitting(msj_out,payload)
        print("message retransmitted...",new_message)
        #start=time.time()
        #thread1=Thread(target=threaded_send,args=(msj_out,s))
        #thread1.start()
        #print("------------")
        #thread1.join()

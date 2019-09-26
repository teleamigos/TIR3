"""-----------------------------------------------------------------------------
---------------------------This is thread file----------------------------------
-----------------------------------------------------------------------------"""
import time
from threading import Thread
def threaded_send(msj,s):
    print("Your message is being sent.")
    time.sleep(1)
    print("to send : ",msj)
    s.sendall(msj)
    print("Your message was sent.")

def Type_info_new(F,s):
    dst_user=input("Type the user you want to send something (A,B,C or D) : " )
    message=input("Type a message you want to send to {} with ID {} :".format(dst_user,F.user[dst_user]))
    payload=F.create_payload(dst_user,message)
    print("payload : ",payload)
    msj_out=F.create_package(F.broadcast,F.my_add,payload)
    print("Message to ID {}  and sequence {} to send  : ".format(F.user[dst_user],F.sequence),msj_out)
    """start=time.time()
    thread1=Thread(target=threaded_send,args=(msj_out,s))
    thread1.start()
    thread1.join()"""

def Type_info_reply(F,s,dst_add):
    dst_user=input("type the user you want to reply : ")
    message=input("Type a message you want to send to {} with ID {} :".format(dst_user,F.user[dst_user]))
    F.sequence +=1
    payload=F.create_payload(dst_user,message)
    print("payload : ",payload)
    msj_out=F.create_package(F.broadcast,F.my_add,payload)
    print("Message to ID {}  and sequence {} to send  : ".format(F.user[dst_user],F.sequence),msj_out)
    start=time.time()
    """thread1=Thread(target=threaded_send,args=(msj_out,s))
    thread1.start()
    thread1.join()"""

"""-----------------------------------------------------------------------------
---------------------------This is thread file----------------------------------
-----------------------------------------------------------------------------"""
import time
def threaded_send(msj,s):
    print("Your message is being sent.")
    time.sleep(1)
    print("to send : ",msj)
    s.sendall(msj)
    print("Your message was sent.")

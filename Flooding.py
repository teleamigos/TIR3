from struct import *
import zlib

"""----------------------class flooding-----------------------------------------
-----------------------------------------------------------------------------"""

class Flooding:
    def __init__(self,my_usr):
        """class initialization"""
        self.user={
        'A' : 255,
        'B' : 260,
        'C' : 300,
        'D' : 400
        }
        self.my_add=b'\x94\x53\x30\x44\xca\x7f'
        self.broadcast=b'\xff\xff\xff\xff\xff\xff'
        self.my_ID=self.user[my_usr]
        self.ethertype=b'\x08\x01'
        self.sequence=0
        self.message_h=[]

    def create_payload(self,usr_dst,message):
        payload=pack('!QH',self.sequence,self.user[usr_dst])
        payload += bytes(message,'utf-8')
        return payload

    def create_package(self,dst_add,src_add,payload):
        crc=pack('!I',zlib.crc32(payload))
        msj_out=dst_add+src_add+self.ethertype+payload+crc
        print(msj_out)
        return msj_out

    def Unpack_message(self,msj):
        L=len(msj)
        ID=unpack('!H',msj[22:24])[0]
        if ID==self.my_ID:
            """This message is for me!!"""
            payload=msj[14:L-4]
            ID,msj_rcved=self.Unpack_payload(payload)
            self.message_h.append((msj_rcved,self.sequence,ID))
            print("IN THE HISTORY : ",self.message_h)
            return ID, msj_rcved,msj[6:12]
        else:
            """This message is not for me!!!"""
            return '0'

    def retransmitting(self,msj,payload):
        seq=unpack('!Q',payload[:8])[0]
        ID=unpack('!H',payload[8:10])[0]
        message=payload[10:].decode('utf-8')
        seq +=1
        for u in self.user:
            if self.user[u]==ID:
                dst_user=u
        self.sequence +=seq
        new_payload=self.create_payload(dst_user,message)
        dst_add=msj[:6]
        src_add=msj[6:12]
        new_msj=self.create_package(dst_add,src_add,new_payload)
        return new_msj

    def Unpack_payload(self,payload):
        self.sequence,ID=unpack('!QH',payload[:10])
        message=payload[10:].decode('utf-8')
        return ID,message

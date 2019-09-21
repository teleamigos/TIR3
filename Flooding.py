from struct import *
import zlib
#import crc16

"""----------------------class flooding---------------------------
---------------------------------------------------------------"""

class Flooding:
    def __init__(self,my_usr):
        self.user={
        'A': b'\xc8\xe0\xeb\x38\xc8\xd3',
        'B': b'\xc8\xe0\xeb\x38\xc8\xd3',
        'C': b'\xc8\xe0\xeb\x38\xc8\xd3',
        'D': b'\xc8\xe0\xeb\x38\xc8\xd3'
        }
        """class initialization"""
        self.src_add=""
        self.dst_add=""
        self.ethertype=b"\x08\x01"
        self.payload=""
        self.crc=""
        self.my_add=self.user[my_usr]


    def create_payload(self,id,msj):
        """Creating a payload"""
        L=len(msj)+3#La longitud del mensaje mas tres bytes, uno ID y dos de long.
        self.payload=pack('!BH',id,L)+bytes(msj,'utf-8')#Concatena ID, long y msj.
        print("payload for this package : ",self.payload)

    def create_package(self,src,dst):
        """Creating a package"""
        self.src_add=self.user[src]
        self.dst_add=self.user[dst]#Direccion MAC destino
        self.crc=pack('!I',zlib.crc32(self.payload))#Calcula CRC32
        msj_out=self.dst_add+self.src_add+self.ethertype+self.payload+self.crc
        print("To send : ",msj_out)
        return msj_out

    def Unpack_message(self,msj_rcved):
        """Unpack the message received"""
        print("message received : ",msj_rcved)
        L=len(msj_rcved)
        self.dst_add=msj_rcved[0:6]
        if self.dst_add==self.my_add:
            """the direction is correct"""
            self.src_add=msj_rcved[7:12]
            data=self.Unpack_payload(msj_rcved[14:L-4])
            self.crc=unpack('!I',msj_rcved[L-4:])
            return data
        else :
            """The direction is wrong"""
            print("Message received is not for this computer...")
            print("retransmiting...")
            return '0'

    def Unpack_payload(self,payload_rcved):
        """Unpack payload"""
        print("payload received : ",payload_rcved)
        ID,L=unpack('!BH',payload_rcved[0:3])
        print(ID,L)
        msj=payload_rcved[3:].decode('utf-8')
        return ID,msj

    def Increase_ID(self,message):
        """Increase the ID of the message"""
        ID=unpack('!B',message[15:16])[0]
        print("ID :" ,ID)

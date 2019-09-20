from struct import *
import zlib
#import crc16

"""----------------------class flooding---------------------------
---------------------------------------------------------------"""

class Flooding:
    def __init__(self,add):
        self.user={
        'A': b'\xc8\xe0\xeb\x38\xc8\xd3',
        'B': b'\xc8\xe0\xeb\x38\xc8\xd3',
        'C': b'\xc8\xe0\xeb\x38\xc8\xd3',
        'D': b'\xc8\xe0\xeb\x38\xc8\xd3'
        }
        """class initialization"""
        self.src_add=self.user[add]
        self.dst_add=""
        self.ethertype=b"\x08\x01"
        self.payload=""
        self.crc=""
        print(self.src_add)

    def create_payload(self,id,msj):
        """Creating a payload"""
        L=len(msj)+3#La longitud del mensaje mas tres bytes, uno ID y dos de long.
        self.payload=pack('!BH',id,L)+bytes(msj,'utf-8')#Concatena ID, long y msj.
        print("payload for this package : ",self.payload)

    def create_package(self,dst):
        """Creating a package"""
        self.dst_add=self.user[dst]#Direccion MAC destino
        self.crc=pack('!I',zlib.crc32(self.payload))#Calcula CRC32
        msj_out=self.dst_add+self.src_add+self.ethertype+self.payload+self.crc
        print("To send : ",msj_out)
        return msj_out

    def Unpack_message(self):
        """Unpack the message received"""
        pass

    def Unpack_payload(self):
        """Unpack payload"""
        pass

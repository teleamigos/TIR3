from Flooding import *

"""---------------------------------------------------------------
----------------This file is ONLY a test-----------------------"""

src=input("Type your user : ")
dst=input("Type a destination : ")
message=input("Type a message : ")


F=Flooding(src)#Inicializa el objeto solo con la direccion en la que nos conectamos
F.create_payload(1,message)#Crea payload con Id por defecto
msj_out=F.create_package(src,dst)#Mensaje de salida

"""-----------------unpacking------------------"""

F.Unpack_message(msj_out)
ID=F.Increase_ID(msj_out)

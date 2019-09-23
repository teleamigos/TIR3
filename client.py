import socket

a="hola"
a_b=bytes(a,'utf-8')
a_h=a_b.hex()

print(a,a_b,a_h)

host = 'localhost'
port = 3000
client = socket.socket()
client.connect((host,port))
client.sendall(a_h.encode('utf-8'))
client.close()

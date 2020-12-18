import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234)) 

s.listen(5)
clt, adr = s.accept()

print("Connection has been established with ",adr)
clt.send(bytes("NSU 338 Lab Server", "utf-8 "))

name= clt.recv(100)
print("User's name is "+name.decode("utf-8"))
while True:
    msg = input("Server:")
    clt.send(bytes(msg,"utf-8"))
    recvmsg = clt.recv(100)
    print("Client: "+recvmsg.decode("utf-8"))
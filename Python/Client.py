import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
msg = s.recv(100) #Receiving the input sent by server. 100 represent how many bytes it will receive
print(msg.decode("utf-8"))
consoleinput=input("Your Name_")
s.send((bytes(consoleinput, "utf-8 ")))
#transforming the bytes into string again to print
while True:
    recvmsg = s.recv(100)
    print("Server: "+recvmsg.decode("utf-8"))
    msg = input("Client:")
    s.send(bytes(msg, "utf-8"))
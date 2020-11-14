import socket
HEADER=64
PORT=5050
DISSCONNECT_MSG="!Disconnect"
#SERVER='192.168.0.108'
SERVER=SERVER=socket.gethostbyname(socket.gethostname())
FORMAT="utf-8"
ADDR=(SERVER,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length=str(msg_length).encode(FORMAT)
    send_length+=b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
connected =True
while connected:
    uip=input("enter the message bro:")
    send(uip)
    print(client.recv(1024))
    if(uip==DISSCONNECT_MSG):
        connected =False

import socket
import threading

HEADER =64
DISCONNECT_MSG="!Disconnect"
FORMAT='utf-8'
PORT = 5050
#SERVER="192.168.0.108"
SERVER=socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR=(SERVER,PORT)
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print('[NEW CONNECTION] {} connected now'.format(addr))
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if(msg.lower()=="how are you?"):
                conn.send(bytes("I am ALive!!",FORMAT))
            elif(msg==DISCONNECT_MSG):
                conn.send(bytes("u disconnected" ,FORMAT))
                connected =False
            elif(msg.lower()=="what is your name?"):
                conn.send(bytes("I am Test Server",FORMAT))
            elif(msg.startswith("a")):
                num=msg.split(" ")
                res=int(num[1]) + int(num[3])
                conn.send(bytes("the added result is:{}".format(res),FORMAT))
            else:
                conn.send(bytes("SOrry i dont understand tht:",FORMAT))
            print("[{}] sent {}".format(addr,msg))
            
    conn.close()
    print("{} is now disconnected".format(addr))
    


def start():
    server.listen()
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        count=threading.active_count()
        print("[ACTIVE CONN]:{}".format(count-1))


print("[STARTING] The server is starting")

start()

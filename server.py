import socket
from threading import Thread
from time import sleep
server=socket.socket()
server.bind((socket.gethostbyname(socket.gethostname()),117))
print(f"your ip is: {socket.gethostbyname(socket.gethostname())}")
clients=[]

l=True

def brodcast(msg):
    print("brodcasting")
    print(msg)
    global clients
    for i in clients:
        i.send(msg.encode())

def keep(client):
    global l
    while l:
        sleep(5)
        client.send("hb".encode())



def receive(client):
    global l
    print("receiver online")
    client.send(f"i:{clients.index(client)}".encode())
    while l:
        try:
            msg = client.recv(64).decode()
            if msg:
                msg=msg.split(":")
                if msg != ["hb"]:print(msg)
                if msg[0] == "p":
                    brodcast(f"s:{msg[1]}:{msg[2]}")
                
        except:
            pass

def main():
    global l
    server.listen()
    while True:
        try:
            client,ip=server.accept()
            print(ip)
            clients.append(client)
            keeper=Thread(target=keep,args= (client,))
            receiver=Thread(target=receive ,args=(client,))
            keeper.start()
            receiver.start()
        except:
            pass

print ("starting")
mainer=Thread(target=main)
mainer.start()

while l:
    if input("stop?(y/n)") == "y":
        l=False
        print("please press Ctrl+C to correctly stop")
import socket
from threading import Thread
from time import sleep
server=socket.socket()
server.bind((socket.gethostbyname(socket.gethostname()),120))
print(f"your ip is: {socket.gethostbyname(socket.gethostname())}")

clients={
    "cls":[],
    "closed":[]
}


l=True

def brodcast(msg):
    print("brodcasting")
    print(msg)
    global clients
    for i in clients["cls"]:
        i.send(msg.encode())

def keep(client):
    global closed
    global l
    _closed=True
    while l and _closed:
        client.send("hb".encode())
        sleep(5)
        if clients["closed"][clients["cls"].index(client)] != True:
            _closed=False
            client.close()



def receive(client):
    global l
    bruh=True
    global closed
    print("receiver online")
    client.send(f"i:{ clients['cls'].index(client)}".encode())
    while l and bruh:
        try:
            msg = client.recv(64).decode()
            if msg:
                msg=msg.split(":")
                if msg != ["hb"]:print(msg)
                if msg[0] == "p":
                    brodcast(f"s:{msg[1]}:{msg[2]}")
                if msg[0] == "quit":
                    index=clients["cls"].index(client)
                    clients["closed"].pop(index)
                    clients["closed"].insert(index,False)
        except:
            pass

def main():
    global l
    server.listen()
    while True:
        try:
            client,ip=server.accept()
            print(ip)
            clients["cls"].append(client)
            clients["closed"].append(True)
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
#this is a nightmare
import socket
from threading import Thread
from time import sleep
import renderer
client=socket.socket()
client.connect((input("input server ip"),117))
sleep(5)

id=None

def keeper():
    while True:
        sleep(5)
        client.send("hb".encode())
def receive(server):
    global id
    while True:
        try:
            msg = server.recv(64).decode()
            if msg:
                msg = msg.split(":")
                if msg != ["hb"]:print(msg)
                if msg[0] == "i":
                    id=int(msg[1])
                if msg[0]=="s":
                    print("rendering")
                    renderer.ren.append(renderer.rendered((0,0,255),eval(msg[1]),renderer.size/80))
        except:
            pass

Thread(target=keeper).start()
Thread(target=receive,args=(client,)).start()
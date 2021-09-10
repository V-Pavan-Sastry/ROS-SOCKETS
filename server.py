import socket
import threading

HEADER= 64
PORT= 5050
#SERVER ="192.168.146.1"
SERVER = socket.gethostbyname(socket.gethostname())
#print(SERVER)
FORMAT='utf-8'
ADDR = (SERVER,PORT)
DISCONNECT_MESSAGE="!DISCONNECT"




server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:

            msg_length= int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            print(f"[{addr}] : {msg}")
            conn.send("Message received ".encode(FORMAT)) 
            if msg==DISCONNECT_MESSAGE:
            
                print(f"[DISCONNECTED] From [{addr}]")
                conn.send("you are now disconnected".encode(FORMAT))
                connected=False
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is Listening on {SERVER}")
    while True:
        conn,addr = server.accept()
        thread=threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() -1}" )

print("[STARTING] Server is Starting .......")
start()


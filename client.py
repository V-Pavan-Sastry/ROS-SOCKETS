import socket

HEADER= 64
PORT = 5050
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER= socket.gethostbyname(socket.gethostname())
ADDR= (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
print(f"Connected to the server: {ADDR}")
def send(msg):
    message=msg.encode(FORMAT)
    msg_length = len(message)
    send_length= str(msg_length).encode(FORMAT)
    send_length += b' ' *(HEADER -len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
def send_text():
    MeSSage= input("Enter the message to be sent to the Server :\n")
    send(MeSSage)

send_text()
a=True
while a==True:
    status_check= input("Enter D to Disconnect from the server or any key to Continue")
    if status_check=='d' or status_check=='D':
        send(DISCONNECT_MESSAGE)
        a=False
    else:
        send_text()

print(f"DISCONNECTED FROM the Server")

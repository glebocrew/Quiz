import socket

from colorama import Fore as foreground
from colorama import Back as background
from colorama import Style as style

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#HOST = socket.gethostbyname(socket.gethostname())
HOST = "127.0.0.1"
PORT = 65432

server_sock.bind((HOST, PORT))
print(f"Running on {HOST} : {PORT}")


while True:
    server_sock.listen()
    client_sock, client_address = server_sock.accept()
    data = client_sock.recv(1024)
    
    data_array = str(data)[2:len(str(data))-1].split(sep=':')
    if data_array[2] == "GET":
        print(foreground.GREEN + f"{data_array[3]}")
        print(style.RESET_ALL)

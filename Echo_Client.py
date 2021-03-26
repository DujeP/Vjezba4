# -- coding: utf-8 --
#echo_client.py
import socket
import datetime

host = socket.gethostname()
port = 12345
client_socket = socket.socket() # TCP scoket

client_socket.connect((host,port))
#clientSocket.sendto(message.encode(),(serverName, serverPort))
#client_socket.sendto("Tekst koji se salje".encode())
unos = input("Sto zelite da se ispise?")
while unos.upper() == "DUJE POPOVIC":
    print("Unos nije podrzan")
    unos = input("Sto zelite da se ispise?")
client_socket.sendall(str(unos).encode())

data = client_socket.recv(1024) # Tekst koji je primljen od servera

print(data) #ispis podataka
print(datetime.datetime.now())
client_socket.close() #close the connection
# -- coding: utf-8 --
#echo_server.py
import socket
import datetime
from Local_Machine_Info import print_machine_info
print_machine_info()

host = socket.gethostname()
port = 12345

echo_server = socket.socket()# TCP socket
echo_server.bind((host,port))
echo_server.listen(5)

print("Cekam Klijenta...")
echo_server.listen(5)
conn, addr = echo_server.accept() # Prihvacanje konekcija kada se klijent spoji
print("Spojen: ", addr)
print(datetime.datetime.now())

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)

conn.close()
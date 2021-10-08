#!/usr/bin/env python3

import socket
from random import seed
from random import randint
import threading

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
ADDR = (HOST, PORT)
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('listening..')


def answer(conn):
 numbers = b''
 numbers = conn.recv(1024)
 numbers = numbers.decode('ascii')
 numbers = int(numbers)
 
 for _ in range(1):
    dice = randint(1, 6)
    print('dice: ', dice)
    print('numbers: ', numbers)

 
 if dice == numbers:
   conn.send(bytes(f"You WON, the value of the dice was {dice}", encoding=FORMAT))
 else:
   conn.send(bytes(f"You LOSE, the value of the dice was {dice}", encoding=FORMAT))


while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    print('conn: ', conn)
    threading.Thread(target=answer, args=[conn]).start()
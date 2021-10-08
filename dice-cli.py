#!/usr/bin/env python3

import socket
from random import seed
from random import randint
import threading


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
ADDR = (HOST, PORT)
FORMAT = "utf-8"


while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    print('CASINO')
    number = int(input('Choose your number in dice (between 1 and 6): '))

    if number == 0:
        exit
    if number == 1:
        s.sendall(b'1')
        break
    if number == 2:
        s.sendall(b'2')
        break
    if number == 3:
        s.sendall(b'3')
        break
    if number == 4:
        s.sendall(b'4')
        break
    if number == 5:
        s.sendall(b'5')
        break
    if number == 6:
        s.sendall(b'6')
        break


data = s.recv(1024)
length = len(data)
dice = data[length -1]

if dice == 49:
   print('-----')
   print('|   |')
   print('| o |')
   print('|   |')
   print('-----')


if dice == 50:
   print('-----')
   print('|o  |')
   print('|   |')
   print('|  o|')
   print('-----')


if dice == 51:
   print('-----')
   print('|o  |')
   print('| o |')
   print('|  o|')
   print('-----')


if dice == 52:
   print('-----')
   print('|o o|')
   print('|   |')
   print('|o o|')
   print('-----')


if dice == 53:
   print('-----')
   print('|o o|')
   print('| o |')
   print('|o o|')
   print('-----')

if dice == 54:
   print('-----')
   print('|o o|')
   print('|o o|')
   print('|o o|')
   print('-----')


print('Received', repr(data))

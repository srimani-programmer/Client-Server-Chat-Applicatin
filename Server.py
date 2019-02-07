# Chat Application Server Code.
# done by @Sri_Programmer.
# Python v3.x

__author__ = 'Sri Manikanta Palakollu.'

import socket
import time

host = '127.0.0.1'
port = 5000

clients_list = []

socket_obj = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_obj.bind((host,port))
socket_obj.setblocking(0)

quit_value = False
print('Server Started')

while not quit_value:

    try:
        data,address = socket_obj.recvfrom(1024)

        if "Quit" in str(data):
            quit_value = True
        
        if address not in clients_list:
            clients_list.append(address)
        
        print(time.ctime(time.time()) + str(address) + ": :" + str(data))

        for client in clients_list:
            socket_obj.sendto(data,client)

    except : pass

socket_obj.close()

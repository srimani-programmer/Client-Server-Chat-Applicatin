# Chat Application Client Code.
# done by @Sri_Programmer.
# Python v3.x

__author__ = 'Sri Manikanta Palakollu.'

import socket
import threading
import time

thread_lock = threading.Lock()
shutdown = False

def receiveMessage(name, sock):
    while not shutdown:
        try:
            thread_lock.acquire()
            while True:
                data,addr = sock.recvfrom(1024)
        except:
            pass
        finally:
            thread_lock.release()

host = '127.0.0.1'
port = 0

server = ('127.0.0.1',5000)

socket_obj = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_obj.bind((host,port))
socket_obj.setblocking(0)

receiving_thread = threading.Thread(target=receiveMessage, args=('RecvThread',socket_obj))
receiving_thread.start()

name = input('Enter the name:')
message = input(name + " : ")

while message != 'q':
    if message != ' ':
        message = (name + " : " +message).encode('utf-8')
        socket_obj.sendto(message, server)
    
    thread_lock.acquire()
    message = input(name + ' : ')
    thread_lock.release()
    time.sleep(0.2)

shutdown = True

receiving_thread.join()
socket_obj.close()

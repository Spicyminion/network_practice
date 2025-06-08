import socket
from _thread import *
import sys

server = "192.168.1.95"  # use ipconfig in command prompt to find IP address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("waiting for connection, server stated")

def read_pos(str):
    str = str.split(',')
    return int(str[0]), int(str[1])  # return two values

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0, 0), (100, 100)]

def threaded_client(conn, player):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048) # how many bits
            reply = data.decode("utf-8") # need to encode info in specific format to send, thus need to decode
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

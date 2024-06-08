import socket
import keyboard
import time
HOST = "192.168.1.186"  # pc private ip
PORT = 50000    
print("Server started at this IP:", HOST)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

conn1, addr1 = s.accept()
print(addr1)
conn1.sendall(b"hi")
print(conn1.recv(1024))
y=0
while 1:
    if y==0:
        conn1.sendall(b"0")
    if keyboard.is_pressed("w"):
        conn1.sendall(b"w")
    if keyboard.is_pressed("a"):
        conn1.sendall(b"a")
    if keyboard.is_pressed("s"):
        conn1.sendall(b"s")
    if keyboard.is_pressed("d"):
        conn1.sendall(b"d")
    if keyboard.is_pressed("f"):
        conn1.sendall(b"f")
    if keyboard.is_pressed("space"):
        conn1.sendall(b"t")
    if keyboard.is_pressed("y"):
        y=1
        conn1.sendall(b"y")

    if keyboard.is_pressed("q"):
        conn1.sendall(b"q")
        break
    time.sleep(0.05)


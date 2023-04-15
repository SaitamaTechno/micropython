import socket
import threading
import time
import cv2
import numpy as np
#HOST = socket.gethostbyname(socket.gethostname())   # Symbolic name meaning all available interfaces
HOST = "192.168.1.186"   # Symbolic name meaning all available interfaces

PORT = 50000              # Arbitrary non-privileged port
print("Server started at this IP:", HOST)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

conn1, addr1 = s.accept()
print(addr1)
e=0
prev_frame_time = 0
new_frame_time = 0

while 1:
    try:
        data1 = conn1.recv(5000)#1024 bytes
        recvd_img=np.array(bytearray(data1), dtype="uint8")
        recvd_img=cv2.imdecode(recvd_img, cv2.IMREAD_COLOR)
        cv2.imshow("sa", recvd_img)
        cv2.waitKey(1)
        conn1.sendall(b'!')
    except cv2.error:
        e+=1    
        print("Errors:", e)
    
import socket
import time
import pyautogui

HOST = "192.168.1.186"  # pc private ip
PORT = 50000    
print("Server started at this IP:", HOST)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

conn1, addr1 = s.accept()
print(addr1)
m=20
conn1.sendall(b'start')
while 1:
    data1 = conn1.recv(1).decode("utf-8")
    try:
        if data1=="w":
            pyautogui.move(0,-m)
        if data1=="s":
            pyautogui.move(0,m)
        if data1=="a":
            pyautogui.move(-m,0)
        if data1=="d":
            pyautogui.move(m,0)
        if data1=="e":
            pyautogui.click()
    except pyautogui.FailSafeException:
        print("errorrrrrrrrrrrrrrrrrr")
        pass
    print(data1)

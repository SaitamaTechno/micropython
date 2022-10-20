import socket
import time
import pyautogui

HOST = "192.168.1.186" #pc private ip
PORT = 50000
print("Server started at this IP:", HOST)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

conn1, addr1 = s.accept()
print(addr1)
m=20
t=0.001
conn1.sendall(b'start')
while 1:
    data1 = conn1.recv(1).decode("utf-8")
    try:
        if data1=="w":
            pyautogui.keyDown("w")
            time.sleep(0.01)
            pyautogui.keyUp("w")
        if data1=="s":
            pyautogui.keyDown("s")
            time.sleep(t)
            pyautogui.keyUp("s")
        if data1=="a":
            pyautogui.keyDown("a")
            time.sleep(t)
            pyautogui.keyUp("a")
        if data1=="d":
            pyautogui.keyDown("d")
            time.sleep(t)
            pyautogui.keyUp("d")
        if data1=="e":
            pyautogui.keyDown("e")
            time.sleep(t)
            pyautogui.keyUp("e")
    except pyautogui.FailSafeException:
        print("errorrrrrrrrrrrrrrrrrr")
        pass
    print(data1)

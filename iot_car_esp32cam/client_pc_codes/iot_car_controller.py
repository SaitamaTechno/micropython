import socket
import keyboard
import time
import threading
def live_stream():
    import live_camera_server
threading.Thread(target=live_stream).start()
HOST = "139.162.186.69"
#HOST = '192.168.1.186'    # The remote host
PORT = 50000              # The same port as used by the server
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("connected")
s.sendall(b"hi")
print(s.recv(1024))
print("car is connected")
y=0
s.settimeout(5)
while 1:
    try:
        if y==0:
            s.sendall(b"0")
        if keyboard.is_pressed("w"):
            s.sendall(b"w")
        if keyboard.is_pressed("a"):
            s.sendall(b"a")
        if keyboard.is_pressed("s"):
            s.sendall(b"s")
        if keyboard.is_pressed("d"):
            s.sendall(b"d")
        if keyboard.is_pressed("f"):
            s.sendall(b"f")
        if keyboard.is_pressed("space"):
            s.sendall(b"t")
        if keyboard.is_pressed("l"):
            s.sendall(b"l")
        if keyboard.is_pressed("y"):
            y=1
            s.sendall(b"y")

        if keyboard.is_pressed("q"):
            s.sendall(b"q")
            break
        time.sleep(0.05)
    except Exception as e:
        print(e)
        break
print("finished")

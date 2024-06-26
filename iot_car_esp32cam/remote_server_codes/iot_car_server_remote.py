import socket
import time
import threading
def live_stream():
    import live_camera_server_remote
threading.Thread(target=live_stream).start()

HOST = "0.0.0.0"  # pc private ip
PORT = 50000    
print("Server started at this IP:", HOST)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
#s.settimeout(30)
client, addr1 = s.accept()
print(addr1)
car, addr2 = s.accept()
print(addr2)

data=client.recv(1024)
car.sendall(data)
data=car.recv(1024)
client.sendall(data)

client.settimeout(5)
car.settimeout(5)

while 1:
    try:
        data=client.recv(1)
        car.sendall(data)
        if b'q' in data:
            break
        time.sleep(0.001)
    except Exception as e:
        print(e)
        break
#time.sleep(3)
s.close()
print("finished")

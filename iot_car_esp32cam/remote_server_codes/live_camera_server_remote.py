import socket
import time

#HOST = socket.gethostbyname(socket.gethostname())   # Symbolic name meaning all available interfaces
HOST = "0.0.0.0"   # Symbolic name meaning all available interfaces

PORT = 50001              # Arbitrary non-privileged port
print("Server started at this IP:", HOST)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
#s.settimeout(600)
quit=0
while quit==0:
    print("First Loop Started")
    client, addr1 = s.accept()
    print("client:", addr1)

    car, addr2 = s.accept()
    print("car:", addr2)

    data=client.recv(2)
    client.sendall(b'!')

    client.settimeout(5)
    car.settimeout(5)
    
    prev_frame_time = 0
    new_frame_time = 0

    while quit==0:
        try:

            data1=b''
            while 1:
                data1 += car.recv(1024)#1024 bytes
                if b'SaitamaTechno' in data1:
                    break
                elif b'reset_connection' in data1:
                    car.close()
                    client.close()
                    break
            client.sendall(data1)

            data=client.recv(1)
            car.sendall(data)
            #data1=b''
            #while 1:
            #    data1+=car.recv(1024)
            #    if b'SaitamaTechno' in data1:
            #        break
            #client.sendall(data1)

            #data=client.recv(1)
            #car.sendall(data)

            if b'q' in data:
                quit=1
        except Exception as e:
            print("Camera connection is lost!")
            client.close()
            car.close()
            quit=1
#time.sleep(3)
s.close()
print("finished")





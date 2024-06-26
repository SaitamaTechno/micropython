import socket
import cv2
import numpy as np
import keyboard
import time

def display_time(seconds):
    """Format and display the time in hours, minutes, seconds format."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

#HOST = socket.gethostbyname(socket.gethostname())   # Symbolic name meaning all available interfaces
HOST = "139.162.186.69"
#HOST = "192.168.1.186"   # Symbolic name meaning all available interfaces
PORT = 50001              # The same port as used by the server
t1=time.time()
quit=0
while quit==0:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    prev_frame_time = 0
    new_frame_time = 0
    s.sendall(b'hi')
    s.recv(1)

    s.settimeout(5)
    while quit==0:
        try:
            data1=b''
            while 1:
                #print(i)
                #s.settimeout(1)
                data1 += s.recv(1024)#1024 bytes
                if b'SaitamaTechno' in data1:
                    data1=data1.replace(b'SaitamaTechno', b'')
                    break
            recvd_img=np.array(bytearray(data1), dtype="uint8")
            recvd_img=cv2.imdecode(recvd_img, cv2.IMREAD_COLOR)
            recvd_img = cv2.resize(recvd_img, (recvd_img.shape[1] * 2, recvd_img.shape[0] * 2), interpolation=cv2.INTER_LINEAR)
            #print("image received")
            #s.sendall(b'!')
            #data1=b''
            #while 1:
            #    data1+=s.recv(16)
            #    #print(data1)
            #    if b'SaitamaTechno' in data1:
            #        data1=data1.replace(b'SaitamaTechno', b'')
            #        break
            #vcc_value = data1.decode("utf-8")
            #vcc_value = round(int(vcc_value)/1024,2)
            #cv2.putText(recvd_img, f"Voltage: {vcc_value}", (0,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255))
            t2=time.time()
            active_time=display_time(t2-t1)

            cv2.putText(recvd_img, f"Active Time: {active_time}", (0,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255))

            cv2.imshow("sa", recvd_img)
            cv2.waitKey(1)
            if keyboard.is_pressed("q"):
                s.sendall(b"q")
                quit=1
            else:
                s.sendall(b'!')
        except Exception as e:
            print(e)
            s.close()
            quit=1
        time.sleep(0.01)
print("finished")


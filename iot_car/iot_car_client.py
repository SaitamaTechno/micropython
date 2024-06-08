import machine
import time
import socket

HOST = '192.168.1.186'    # The remote host
PORT = 50000              # The same port as used by the server
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data=s.recv(2)
print(data)
led=machine.Pin(2)
for i in range(10):
    if (i // 2)==0:
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.1)
led.value(0)
s.sendall(b'hi')
print("Sent hi")

p4 = machine.Pin(2, machine.Pin.OUT)
servo = machine.PWM(p4,freq=50) # freq must be 50Hz for servos
motor_forward = machine.Pin(13, machine.Pin.OUT)
motor_backward = machine.Pin(12, machine.Pin.OUT)
motor_forward.value(0)
motor_backward.value(0)
t=0.05
command_list=[]
item=0
run_command=0
while 1:
    if run_command==0:
        data=s.recv(1)
        if b"y" in data:
            run_command=1
        str_data=data.decode("utf-8")
        command_list.append(str_data)
    elif run_command==1:
        if item==len(command_list):
            run_command=0
            item=0
            data=b"q"
        data=command_list[item].encode("utf-8")
        if data==b"y":
            data=b"q"
        item+=1
        time.sleep(0.01)
        
    
    print(data)
    if b"w" in data:
        motor_forward.value(1)
        motor_backward.value(0)
        time.sleep(t)
        motor_forward.value(0)
        motor_backward.value(0)
    elif b"s" in data:
        motor_forward.value(0)
        motor_backward.value(1)
        time.sleep(t)
        motor_forward.value(0)
        motor_backward.value(0)
    elif b"t" in data: #space stop
        motor_forward.value(0)
        motor_backward.value(0)
        time.sleep(t)
    if b"a" in data:
        servo.duty(64)
    elif b"d" in data:
        servo.duty(94)
    elif b"f" in data:
        servo.duty(77)
    if b"q" in data:
        break
    
servo.deinit()
motor_forward.value(0)
motor_backward.value(0)

#f=open("command_list.txt", "w")
#for i in command_list:
#    f.write(i)
#f.close()
    


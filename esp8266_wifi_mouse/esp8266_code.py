import socket
import time
import network
from machine import Pin, I2C

#machine.freq(80000000)

wlan=network.WLAN(network.STA_IF)
wlan.active(True)

enter = Pin(16, Pin.IN)
down = Pin(12, Pin.IN)
up = Pin(13, Pin.IN)
right = Pin(14, Pin.IN)
left = Pin(15, Pin.IN)

def connect_wifi(wifi, password):
    while wlan.isconnected()==False:
        print("I am trying...")
        wlan.active(False)
        wlan.active(True)
        wlan.connect(wifi, password)
        time.sleep(5)
connect_wifi("yourwifiname", "yourpassword")
print("connected")
HOST = '192.168.1.186'    # The remote host
PORT = 50000              # The same port as used by the server
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

t=0.05
while 1:
    if up.value()==1:
        msg="w".encode("utf-8")
        s.send(msg)
        time.sleep(t)
    if down.value()==1:
        msg="s".encode("utf-8")
        s.send(msg)
        time.sleep(t)
    if left.value()==1:
        msg="a".encode("utf-8")
        s.send(msg)
        time.sleep(t)
    if right.value()==1:
        msg="d".encode("utf-8")
        s.send(msg)
        time.sleep(t)
    if enter.value()==1:
        msg="e".encode("utf-8")
        s.send(msg)
        time.sleep(t)
    time.sleep(0.1)

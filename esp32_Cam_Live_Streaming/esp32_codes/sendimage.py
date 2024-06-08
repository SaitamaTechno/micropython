import socket
import network
import camera_1
import machine

machine.freq(240000000)
#LED = machine.Pin(4, machine.Pin.OUT)
#LED.on()

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('wifi_name', 'wifi_password')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()


HOST = "192.168.1.186"   # Symbolic name meaning all available interfaces
PORT = 50000              # The same port as used by the server
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
while 1:
    a=camera_1.take_photo(62)
    s.sendall(a)
    data = s.recv(10)


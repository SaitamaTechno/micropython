import socket
import network
import camera_1
import machine
import time

vcc = machine.Pin(33, machine.Pin.IN)
vcc = machine.ADC(machine.Pin(33))

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

#do_connect()


HOST = "139.162.186.69"   # Symbolic name meaning all available interfaces
#HOST = "192.168.1.186"   # Symbolic name meaning all available interfaces
PORT = 50001              # The same port as used by the server
quit=0
while quit==0:
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.settimeout(5)
    except Exception as e:
        print("Line 38:", e)
        time.sleep(1)
    while quit==0:
        try:
            a=camera_1.take_photo(10)
            #print(len(a))
            #print(vcc.read())
            s.sendall(a)        
            s.sendall(b'SaitamaTechno')
            data = s.recv(1)
            #vcc_value=vcc.read()
            #s.sendall(str(vcc_value).encode("utf-8"))
            #s.sendall(b'SaitamaTechno')
            #data = s.recv(1)

            if b'q' in data:
                quit=1
        except Exception as e:
            s.close()
            #del s
            print("Line 58:", e)
            #break
            quit=1
camera_1.camera_deinit()


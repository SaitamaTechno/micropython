# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import gc
def free():
    gc.enable()
    print("alloc:", gc.mem_alloc())
    print("free:", gc.mem_free())
    print("collect", gc.collect())
    gc.disable()
def do_connect(wifi, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(wifi, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

wifi_list=sta_if.scan()
for i in wifi_list:
    if i[0]==b'wifi1':
        my_wifi=1
        break
    else:
        my_wifi=0
if my_wifi==1:
    do_connect("wifi1", "pass1")
else:
    do_connect("wifi2", "pass2")

import machine
led = machine.Pin(15, machine.Pin.OUT)#use 4 or 15
led.value(0)

import urequests as requests
r=requests.get("https://saitamatechno.github.io/activate_iot_car/")
programming_mode=int(r.text.replace("programming_mode=", ""))
print(programming_mode)    
if programming_mode==1:
    import webrepl
    webrepl.start()
elif programming_mode==0:
    import iot_car_client

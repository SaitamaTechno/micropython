from touch_lcd import *
import random
from gc9a01 import color565
import time

LCD = LCD_1inch28()
LCD.set_bl_pwm(10000) #brightness max 65535
LCD.fill(LCD.red)
f=open("dbz240.txt", "r")
x,y=0,0
rgb_list=[]
counter=0

for row in f:
    print(counter)
    counter+=1
    for pix in row.split(","):
        rgb_list.append(int(pix))
        if len(rgb_list)==3:
            r,g,b=rgb_list[0], rgb_list[1], rgb_list[2]
            LCD.pixel(x,y, color565(r,b,g)) #b,r,g -> original (max: 31, 31, 63)
            #LCD.pixel(x,y, color565(r,b,g)) #r,b,g -> Best colors!
            
            x+=1
            if x==240:
                x=0
                y+=1
            rgb_list=[]
        #time.sleep(0.001)
    LCD.show()
        
f.close()
#LCD.fill(color565(255,255,0))
LCD.show()


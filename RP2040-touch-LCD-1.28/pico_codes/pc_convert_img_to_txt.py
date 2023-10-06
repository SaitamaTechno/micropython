import cv2
import numpy as np
import time
img=cv2.imread("dbz240.png")

img[:, :, 0] = np.clip(img[:, :, 0] // 8, 0, 31)  # Transform the blue channel (0, 31)
img[:, :, 1] = np.clip(img[:, :, 1] // 4, 0, 63)  # Transform the green channel (0, 31)
img[:, :, 2] = np.clip(img[:, :, 2] // 8, 0, 31)  # Transform the red channel (0, 63)
#cv2.imshow("asd", img)
#cv2.waitKey()
big_list=[]
small_list=[]
for i in img:
    for a in i:
        small_list.append([a[0], a[1], a[2]])
    big_list.append(small_list)
    small_list=[]

f=open("dbz240rgb.txt", "w")
for i in big_list:
    f.write(str(i).replace(str(i)[0], "").replace(str(i)[-1], "").replace(" ", "")+"\n")
f.close()
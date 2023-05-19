import numpy as np
import cv2
from matplotlib import pyplot as plt

def nothing():
    pass

CAMERA_ID = 0

cam = cv2.VideoCapture(CAMERA_ID)
if cam.isOpened() == False:
    print
    'Cannot open the camera-%d' % (CAMERA_ID)
    exit()

cv2.namedWindow('Blur rbg')
cv2.namedWindow('Blur bw')
cv2.namedWindow('Blur default')
cv2.namedWindow('Blur Track bar')

cv2.createTrackbar('blur value', 'Blur Track bar', 3, 21, nothing)
cv2.setTrackbarPos('blur value', 'Blur Track bar', 3)


while(True):
    #camera
    ret, frame = cam.read()
    
    #color change
    pic_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pic_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #blur 홀수 테스트
    ksize1 = cv2.getTrackbarPos('blur value', 'Blur Track bar')
    if(ksize1 % 2==0):
        if(ksize1 == 0):
            ksize1 += 1
        else :
            ksize1 -= 1

    #blur
    res1 = cv2.GaussianBlur(frame, (ksize1,ksize1), 0)
    res2 = cv2.GaussianBlur(pic_rgb, (ksize1,ksize1), 0)
    res3 = cv2.GaussianBlur(pic_bw, (ksize1,ksize1), 0)
    

    #show
    cv2.imshow('Blur rbg', res1)
    cv2.imshow('Blur bw', res2)
    cv2.imshow('Blur default', res3)

    #esc 누르면 종료
    if cv2.waitKey(10) > 0:
        break

cam.release()
cv2.destroyAllWindows()
# 관련 라이브러리 선언
import numpy as np
import cv2
from matplotlib import pyplot as plt
CAMERA_ID = 0
RET = 'o'
cam = cv2.VideoCapture(CAMERA_ID)
if cam.isOpened() == False:
    print
    'Cannot open the camera-%d' % (CAMERA_ID)
    exit()

cv2.namedWindow('CAM Window')

while(True):
    ret, frame = cam.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    frame_blur = cv2.GaussianBlur(gray_frame, (3,3), 0)
    sobel = cv2.Sobel(gray_frame, cv2.FILTER_SCHARR, 1, 0, ksize=3)
    scharr = cv2.Scharr(frame_blur, cv2.CV_32FC1, 0, 1)
    laplacian = cv2.Laplacian(frame_blur, cv2.CV_32FC1)
    
    ret = cv2.waitKey(10)
    if(RET != ret):
        RET = ret
    if RET==ord('a'):
        cv2.imshow('CAM Window', sobel)
    elif RET==ord('b'):
        cv2.imshow('CAM Window', scharr)
    elif RET==ord('c'):
        cv2.imshow('CAM Window', laplacian)
    elif RET==ord('o'):
        cv2.imshow('CAM Window', frame)
    elif RET==ord('g'):
        cv2.imshow('CAM Window', gray_frame)
    elif RET==ord('q'):
        print("Exit")
        break   

cam.release()
cv2.destroyAllWindows()
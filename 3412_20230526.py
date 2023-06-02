# 관련 라이브러리 선언
import numpy as np
import cv2
from matplotlib import pyplot as plt

#--- init params
CAMERA_ID = 0
FIRST = True
MO = None
cam = cv2.VideoCapture(CAMERA_ID)
if cam.isOpened() == False:
    print
    'Cannot open the camera-%d' % (CAMERA_ID)
    exit()

cv2.namedWindow('CAM Window')

def check_mode(RET):
    if RET==ord('a'):
        return(sobel)
    elif RET==ord('b'):
        return(scharr)
    elif RET==ord('c'):
        return(laplacian)
    elif RET==ord('o') or FIRST:
        return(frame)
    elif RET==ord('g'):
        return(gray_frame)
    elif RET==ord('q'):
        print("Exit")
        cam.release()
        cv2.destroyAllWindows()
    else:
        return(frame)


while(True):
    ret, frame = cam.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    frame_blur = cv2.GaussianBlur(gray_frame, (3,3), 0)
    sobel = cv2.Sobel(gray_frame, cv2.FILTER_SCHARR, 1, 0, ksize=3)
    scharr = cv2.Scharr(frame_blur, cv2.CV_32FC1, 0, 1)
    laplacian = cv2.Laplacian(frame_blur, cv2.CV_32FC1)

    ret = cv2.waitKey(1)
    if ret == -1:
        cv2.imshow('CAM Window', MO)
    else:
        cv2.imshow('CAM Window', check_mode(ret))
    if(FIRST):
        FIRST = False
import numpy as np
import cv2
from matplotlib import pyplot as plt

#--- init params
CAMERA_ID = 0
FIRST = True
CLUSTERING_VALUE = 1
BG = None
WCNT = 0
cam = cv2.VideoCapture(CAMERA_ID)
if cam.isOpened() == False:
    print
    'Cannot open the camera-%d' % (CAMERA_ID)
    exit()

cv2.namedWindow('CAM Window')

def check_mode(RET):
    global BG
    # 배경영상 촬영 (캡쳐)
    if RET==ord('q'):
        BG = frame
    # 숫자 입력받기
    elif RET==ord('1'):
        CLUSTERING_VALUE = 1
    elif RET==ord('2'):
        CLUSTERING_VALUE = 2
    elif RET==ord('3'):
        CLUSTERING_VALUE = 3
    elif RET==ord('4'):
        CLUSTERING_VALUE = 4
    elif RET==ord('5'):
        CLUSTERING_VALUE = 5
    # 입력받은 숫자 * 5만큼의 숫자 만큼 배경 영상과 카메라 영상에 K-means clustering 적용
    elif RET==ord('k'):
        return(res)
    # 입력된 영상, 원본
    elif RET==ord('o') or FIRST:
        return(frame)
    # 원래 배경 제거
    elif RET==ord('b'):
        res2 = cv2.absdiff(cv2.cvtColor(BG, cv2.COLOR_BGR2GRAY), cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        return(res2)
    # 나가기
    elif RET==ord('e'):
        print("Exit")
        cam.release()
        cv2.destroyAllWindows()
    else:
        return(frame)
    return 0

while(True):
    #원본
    ret, frame = cam.read()
    # frame = cv2.resize(frame, (320,240))
    if WCNT == 0 :
        BG = frame

    #클러스터링
    data = frame.reshape((-1,3))
    data = np.float32(data)

    criteria = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    attempts = 10
    flags = cv2.KMEANS_RANDOM_CENTERS

    numK = CLUSTERING_VALUE * 5
    ret, label, center = cv2.kmeans(data, numK, None, criteria, attempts, flags)

    center = np.uint8(center)
    res = center[label.flatten()]
    res = res.reshape((frame.shape))
    res2 = frame

    #출력
    ret = cv2.waitKey(1)
    if ret == -1:
        cv2.imshow('CAM Window', frame)
    else:
        cv2.imshow(str(numK), check_mode(ret))
    if(FIRST):
        FIRST = False

    WCNT += 1
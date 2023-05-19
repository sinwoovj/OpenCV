# 관련 라이브러리 선언
import numpy as numpy
import cv2
from matplotlib import pyplot as plt

# 트랙바 호출함수
def nothing(x):
    pass
def check_odd(num):
    if num % 2 ==0:
        num += 1
    return num

# 영상 읽기
img1 = cv2.imread("./img2.jpg", cv2.IMREAD_GRAYSCALE)
img_index = 1
cv2.namedWindow('Morphology')
cv2.createTrackbar('method', 'Morphology', 0, 1, nothing)
cv2.createTrackbar('ksize', 'Morphology', 3, 10, nothing)
cv2.createTrackbar('iter', 'Morphology', 0, 10, nothing)
# cv2.createTrackbar('run', 'Morphology', 0, 1, nothing)
cv2.setTrackbarPos('method', 'Morphology', 0)
cv2.setTrackbarPos('ksize', 'Morphology', 0)
cv2.setTrackbarPos('iter', 'Morphology', 0)
# cv2.setTrackbarPos('run', 'Morphology', 0)
cv2.imshow("Morphology", img1)

while True:
    method = cv2.getTrackbarPos('method',"Morphology")
    itr = cv2.getTrackbarPos('iter', "Morphology")
    ksize = cv2.getTrackbarPos('ksize',"Morphology")
    # run = cv2.getTrackbarPos('run', "Morphology")
    ksize = check_odd(ksize)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (ksize, ksize))
    if method == 0:
        res = cv2.erode(img1, kernel, iterations=itr)
    else:
        res = cv2.dilate(img1, kernel, iterations=itr)
    cv2.imshow("Morphology", res)
    if cv2.waitKey(50) == 27:
        print("End")
        cv2.destroyAllWindows()
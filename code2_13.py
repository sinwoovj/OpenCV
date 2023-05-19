# 사진 파일을 열고 보여주고 저장해보기
import cv2 as cv
import sys

img = cv.imread("puppy.jpg")
if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)

k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("puppy2.jpg", img)
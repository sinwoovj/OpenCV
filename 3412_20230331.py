#3학년 4반 12번 최신우
#배경과 타겟을 subtract하고 binary작업하고 마스크를 이용해서 bitwise_and 한다.

import cv2 as cv
from matplotlib import pyplot as plt

#이미지 불러오기
target = cv.imread('images/target.jpg', cv.IMREAD_GRAYSCALE)
background = cv.imread('images/background.jpg', cv.IMREAD_GRAYSCALE)

# #이미지 흐림처리
# target = cv.medianBlur(target,5)
# background = cv.medianBlur(background,5)


#타겟 추출하기
subimg = cv.subtract(target, background)

#이미지 이진화 하기
ret, mask = cv.threshold(subimg,50,255,cv.THRESH_BINARY_INV)


#원본 target에서 마스크 빼기
result = cv.bitwise_and(target, mask)

#결과 출력하기
titles = ['target', 'background', 'mask', 'result']
imgs   = [target, background, mask, result]

for i in range(4):
    plt.subplot(2,3,i+1)
    plt.imshow(imgs[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
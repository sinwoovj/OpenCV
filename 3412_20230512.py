# 관련 라이브러리 선언
import numpy as np
import cv2
from matplotlib import pyplot as plt

l_x = [] # 왼쪽 아래, 왼쪽 위, 오른쪽 위, 오른쪽 아래
l_y = []

def M_Location(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        l_x.append(x)
        l_y.append(y)

# 영상 읽기
img1 = cv2.imread("./road.jpg", cv2.IMREAD_GRAYSCALE)
img1 = cv2.resize(img1,(320,240))

#마우스 입력
cv2.imshow('image', img1)
for i in range(4):
    cv2.setMouseCallback('image', M_Location)

# 투시 변환 수행
h, w = img1.shape
# 중점은 좌측 상단 // A 왼쪽 위, B 오른쪽 위, C 왼쪽 아래, D 오른쪽 아래
point1_src = np.float32([[l_x[1],l_y[1]], [l_x[2],l_y[2]], [l_x[0],l_y[0]], [l_x[3],l_y[3]]]) 
#A,C 중의 최솟값, B,D중의 최대값을 x 값으로 한다.
if(l_x[1]>l_x[0]):
    left = l_x[0]
else:
    left = l_x[1]
if(l_x[3]>l_x[2]):
    right = l_x[3]
else:
    right = l_x[2]
#A,B 중의 최솟값, C,D중의 최대값을 y 값으로 한다.
if(l_x[1]>l_x[2]):
    up = l_x[2]
else:
    up = l_x[1]
if(l_x[3]>l_x[0]):
    down = l_x[3]
else:
    down = l_x[0]

point1_dst = np.float32([[left,up], [right,up], [left,down],[right,down]])
per_mat1 = cv2.getPerspectiveTransform(point1_src, point1_dst)
res1 = cv2.warpPerspective(img1, per_mat1, (w,h))

# 결과 영상 출력    
ress = [];
ress.append(img1), ress.append(res1)

for i in range(2):
    plt.subplot(2,2,i+1)
    plt.imshow(ress[i], cmap='gray')
    plt.xticks([]), plt.yticks([])

plt.show()
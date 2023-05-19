import cv2 #opencv 라이브러리 가져오기

img = cv2.imread('shurub.png') #imread > 해당 사진을 불러와서 img에 저장함

cv2.imshow('image', img) #imshow > 우리가 볼 수 있도록 창을 띄움 >> imshow('창의 제목', 보고자하는 변수)

cv2.waitKey(0) #키입력을 기다림 > 0 = esc

cv2.destroyAllWindows() #해당 창을 끔.

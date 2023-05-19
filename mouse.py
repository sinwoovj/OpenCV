import cv2
import numpy as np
def draw_rect(event, x, y, flags, param):
    #print(event)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.rectangle(img, (x-25,y-25), (x+25, y+25), (0,255,0),1)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rect)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

cv2.EVENT_LBUTTONUP
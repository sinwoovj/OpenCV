import cv2
import numpy as np

#--- init params
click = False
click2 = False
x1, y1, x2, y2 = -1, -1, -1, -1

#--- mouse callback
def mousePass(event, x, y, flags, param):
    pass

def mouseCallback(event, x, y, flags, param):
    global x1, y1, x2, y2, click, click2, frame

    if event == cv2.EVENT_LBUTTONDOWN:
        click = True
        x1, y1 = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if click :
            cv2.rectangle(frame, (x1, y1), (x, y), (0, 0, 255), 2)
    elif event == cv2.EVENT_LBUTTONUP:
        if click :
            x2, y2 = x, y
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        click2 = True
        print('clicked')

#--- cam setting
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)

windowName = "input"
cv2.namedWindow(windowName)
cv2.setMouseCallback(windowName, mouseCallback)


status, frame = cam.read()
template = frame.copy()

while not click2:
    cv2.imshow(windowName, frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    if click2 == True:
        break


template2 = template[y1:y2, x1:x2]
cv2.namedWindow('template')
cv2.imshow('template', template2)

#--- template matching
w = x2 - x1
h = y2 - y1

method = cv2.TM_CCORR_NORMED

while cam.isOpened():
    status, frame = cam.read()

    res = cv2.matchTemplate(frame, template2, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bottom_right = max_loc[0]+w, max_loc[1]+h

    cv2.rectangle(frame, top_left, bottom_right, (0,0,255), 2)

    if status:
        cv2.imshow(windowName, frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
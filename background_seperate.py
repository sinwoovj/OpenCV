import cv2
import numpy as np

cap = cv2.VideoCapture("./images_/video2.mp4")

bgMethod1 = cv2.createBackgroundSubtractorMOG2()
bgMethod2 = cv2.createBackgroundSubtractorKNN()
bgMethod1_blur = cv2.createBackgroundSubtractorMOG2()
bgMethod2_blur = cv2.createBackgroundSubtractorKNN()

imgIndex = 1
while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is None:
        break
    frame =cv2.resize(frame, (320, 240))
    if imgIndex != 1:
        bgMOG = bgMethod1.getBackgroundImage()
        bgKNN = bgMethod2.getBackgroundImage()
        bgMOG_blur = bgMethod1_blur.getBackgroundImage()
        bgKNN_blur = bgMethod2_blur.getBackgroundImage()
    fgMOG = bgMethod1.apply(frame, learningRate = -1)
    fgKNN = bgMethod2.apply(frame)
    fgMOG_blur = bgMethod1_blur.apply(cv2.blur(frame, (5,5)), learningRate = -1)
    fgKNN_blur = bgMethod2_blur.apply(cv2.blur(frame, (5,5)))

    print(imgIndex)

    cv2.imwrite("output/" + "mog2_" + str(imgIndex) + ".jpg", fgMOG)
    cv2.imwrite("output/" + "knn_" + str(imgIndex) + ".jpg", fgKNN)
    cv2.imwrite("output/" + "mog2_blur_" + str(imgIndex) + ".jpg", fgMOG_blur)
    cv2.imwrite("output/" + "knn_blur_" + str(imgIndex) + ".jpg", fgKNN_blur)

    imgIndex += 1
    cv2.waitKey(30)

    if imgIndex > 100:
        break
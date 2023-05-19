import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("images/img3.jpg", cv2.IMREAD_GRAYSCALE)

ch1 = [0]; ch2 = [0]; ch3 = [0]
ranges1 = [0, 256]; ranges2 = [0, 128]; ranges3 = [128, 256]
histSize1 = [256]; histSize2 = [128]; histSize3 = [128]

hist1 = cv2.calcHist([img1], ch1, None, histSize1, ranges1)
hist2 = cv2.calcHist([img1], ch2, None, histSize2, ranges2)
hist3 = cv2.calcHist([img1], ch3, None, histSize3, ranges3)

bin_x1 = np.arange(256)
bin_x2 = np.arange(128)
bin_x3 = np.arange(128) + 128

plt.title("histogram")
plt.xlabel("Bin")
plt.ylabel("Frequency")
plt.plot(bin_x1, hist1, color='b')
plt.bar(bin_x2, hist2[:,0], width=6,color='r')
plt.bar(bin_x3, hist3[:,0], width=6, color='g')
plt.grid(True, lw = 1, ls = '--', c= '.75')
plt.xlim([0,255])

plt.show()
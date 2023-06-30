import cv2
import numpy as np


img1_src = cv2.imread("./images_/img25.png", cv2.IMREAD_UNCHANGED)

img1 = cv2.resize(img1_src, (320,240))

data = img1.reshape((-1,3))
data = np.float32(data)

criteria = (cv2.TermCriteria_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
attempts = 10
flags = cv2.KMEANS_RANDOM_CENTERS
for i in range(1, 5):
    numK = i * 5
    ret, label, center = cv2.kmeans(data, numK, None, criteria, attempts, flags)

    center = np.uint8(center)
    res = center[label.flatten()]
    res = res.reshape((img1.shape))
    cv2.imshow(str(numK), res)
    cv2.waitKey(0)

cv2.waitKey(0)

cv2.destroyAllWindows()
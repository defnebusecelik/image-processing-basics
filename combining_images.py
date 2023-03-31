import cv2
import numpy as np
img=cv2.imread("test_image.png")
cv2.imshow("Orijinal",img)

hor=np.hstack((img,img))
cv2.imshow("Yatay",hor)

ver=np.vstack((img,img))
cv2.imshow("Dikey",ver)

import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv2.imshow("Siyah Alan",img)

cv2.line(img,(0,0),(512,512),(255,0,0),3)
cv2.imshow("cizgi",img)

cv2.rectangle(img,(15,15),(256,256),(0,0,255),cv2.FILLED)
cv2.imshow("dikdortgen",img)

cv2.circle(img,(300,300),50,(0,255,0),cv2.FILLED)
cv2.imshow("cember",img)

cv2.putText(img,"metin",(350,350),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255))
cv2.imshow("metin",img)

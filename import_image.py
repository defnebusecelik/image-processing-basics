import cv2
img=cv2.imread("img.jpg",0)
cv2.imshow("ilk gorsel",img)
k=cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("imggray.jpg",img)
    cv2.destroyAllWindows()

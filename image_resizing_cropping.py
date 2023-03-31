import cv2
img=cv2.imread("test_image.png")
print("Görsel boyutu: ",img.shape)
#(512,512,3)
cv2.imshow("Orijinal",img)

imgResized=cv2.resize(img,(700,700))
cv2.imshow("Boyutlandirilmis",imgResized)

imgCropped=img[:400,:200]
cv2.imshow("Kirpimis",imgCropped)

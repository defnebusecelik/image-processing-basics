import cv2
import matplotlib.pyplot as plt
img1=cv2.imread("img1.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.imread("img2.jpg")
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)
plt.figure()
plt.imshow(img2)

print(img1.shape)
#836,1278,3
print(img2.shape)
#852,1147,3

img1=cv2.resize(img1,(836,1147))
img2=cv2.resize(img2,(836,1147))

plt.figure()
plt.imshow(img1)
plt.figure()
plt.imshow(img2)

blended=cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
plt.figure()
plt.imshow(blended)

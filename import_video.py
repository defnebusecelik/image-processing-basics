import cv2
import time
video_name="MOT17-04-DPM.mp4"
cap=cv2.VideoCapture(video_name)
print("Genislik: ",cap.get(3))
print("Yükseklik: ",cap.get(4))
#Genislik:  1920.0
#Yükseklik:  1080.0
if cap.isOpened()==False:
    print("Hata!")
while True:
    ret,frame=cap.read()
    if ret==True:
        time.sleep(0.0001)
        cv2.imshow("ilk video", frame)
    else: 
        break
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

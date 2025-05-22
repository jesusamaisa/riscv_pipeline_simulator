import cv2
import numpy as np
import time
import os

output_dir="cropped_parts"
os.makedirs(output_dir,exist_ok=True)

##Cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_righteye_2splits.xml')
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

cap=cv2.VideoCapture(0)
max_photos=10
eye_count=0
face_count=0
mouth_count=0

while True:
    ret,frame=cap.read()
    if not ret:
        break
    if face_count >= max_photos and eye_count >= max_photos and mouth_count >= max_photos:
        print("Collected 10 images of each part. Exiting.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #faces
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]

        if face_count<max_photos:
            face_img= cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imwrite(f"{output_dir}/face_{face_count}.jpg",face_img)
            cv2.imshow("Face",face_img)
            face_count+=1
        #eyes
        eyes=eye_cascade.detectMultiScale(roi_gray,1.1,10)
        for i,(ex,ey,ew,eh) in enumerate(eyes):
          if eye_count<max_photos:
            eye_img=roi_color[ey:ey+eh,ex:ex+ew]
            cv2.imwrite(f"{output_dir}/eye_{eye_count}.jpg",eye_img)
            cv2.imshow("Eye",eye_img)
            eye_count+=1
            break

        #mouth
        mouths=mouth_cascade.detectMultiScale(roi_gray,1.5,11)
        for(mx,my,mw,mh) in mouths:
            if my >h/2 and mouth_count<max_photos:
                mouth_img = roi_color[my:my + mh, mx:mx + mw]
                cv2.imwrite(f"{output_dir}/mouth_{mouth_count}.jpg", mouth_img)
                cv2.imshow("Mouth", mouth_img)
                mouth_count += 1
                break  # Save only one mouth per face

    cv2.imshow('Face,eyes and mouth detection',frame)
    if cv2.waitKey(0)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




# img=cv2.VideoCapture(0)
# img.set(3,640)
# img.set(4,480)
#
# while True:
#     success,image=img.read()
#     cv2.imshow("Video",image)
#     if cv2.waitKey(1)&0xFF==ord('q'):
#         break
#
# img.release()
# cv2.destroyAllWindows()
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
import cv2
import numpy as np
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
#1 for windows, 0 for mac
cap=cv2.VideoCapture(0)

def baseCamera():
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y+h),(x+w,y+h), (0,0,255),2)
            roi_g=gray[y:y+h,x:x+w]
            roi_c=img[y:y+h, x:x+w]
            eyes=eye.detectMultiScale(roi_g)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_c, (ex,ey),(ex+ew,ey+eh),(0,22,0),2)
            cv2.imshow('img',img)
            k = cv2.waitKey(30)&0xff
            if k==27:
                break
    cap.release()
    cv2.destroyAllWindows()
baseCamera()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

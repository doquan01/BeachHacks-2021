# # This is a sample Python script.

# # Press ⌃R to execute it or replace it with your code.
import cv2
import numpy as np

# # This is a sample Python script.

# # Press ⌃R to execute it or replace it with your code.
import cv2
import numpy as np

# face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# smile=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
# mouth_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_mcs_mouth.xml')
# #1 for windows, 0 for mac
# cap=cv2.VideoCapture(0)

# def baseCamera():
#     while True:
#         ret, img = cap.read()
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = face.detectMultiScale(gray,1.3,5)
#         for (x,y,w,h) in faces:
#             cv2.rectangle(img, (x,y),(x+w,y+h), (0,0,255),2)
#             roi_g=gray[y:y+h,x:x+w]
#             roi_c=img[y:y+h, x:x+w]
#             # eyes=eye.detectMultiScale(roi_g)
#             # for (ex,ey,ew,eh) in eyes:
#             #     cv2.rectangle(roi_c, (ex,ey),(ex+ew,ey+eh),(0,22,0),2)
#             cv2.imshow('img',img)
#             k = cv2.waitKey(30)&0xff
#             if k==27:
#                 break
#             mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
#             for (x,y,w,h) in mouth_rects:
#                 y = int(y - 0.15*h)
#                 cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
#                 break
#             c = cv2.waitKey(30)&0xff
#             if c == 27:
#                 break
#     cap.release()
#     cv2.destroyAllWindows()
# baseCamera()

# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_smile.xml')
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'Mouth.xml')

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        mouth = mouth_cascade.detectMultiScale(roi_gray)
        for (mx, my, mw, mh) in mouth:
            cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (0, 0, 255), 2)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()
# mouth_cascade = cv2.CascadeClassifier('./cascade_files/haarcascade_mcs_mouth.xml')
# #1 for windows, 0 for mac
# cap=cv2.VideoCapture(0)

# def baseCamera():
#     while True:
#         ret, img = cap.read()
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = face.detectMultiScale(gray,1.3,5)
#         for (x,y,w,h) in faces:
#             cv2.rectangle(img, (x,y),(x+w,y+h), (0,0,255),2)
#             roi_g=gray[y:y+h,x:x+w]
#             roi_c=img[y:y+h, x:x+w]
#             # eyes=eye.detectMultiScale(roi_g)
#             # for (ex,ey,ew,eh) in eyes:
#             #     cv2.rectangle(roi_c, (ex,ey),(ex+ew,ey+eh),(0,22,0),2)
#             cv2.imshow('img',img)
#             k = cv2.waitKey(30)&0xff
#             if k==27:
#                 break
#             mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
#             for (x,y,w,h) in mouth_rects:
#                 y = int(y - 0.15*h)
#                 cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
#                 break
#             c = cv2.waitKey(30)&0xff
#             if c == 27:
#                 break
#     cap.release()
#     cv2.destroyAllWindows()
# baseCamera()

# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('Mouth.xml')

while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        mouth = mouth_cascade.detectMultiScale(roi_gray)
        for (mx, my, mw, mh) in mouth:
            cv2.rectangle(roi_color, (mx, my), (mx + mw, my + mh), (0, 0, 255), 2)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()

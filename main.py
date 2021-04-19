import cv2

#This method allows to make the shape for face, eyes, mouth, and any features necessary
def shape(img, classifier, scaleFactor, minNeighbors, color, text):
    # Converts camera to gray-scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # takes image and returns the x,y coordinates, width, and height, allowing you to make the rectangles necessary
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords = []
    #gets the x,y, width, and height and uses it to make the face in a continues video
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        #label
        cv2.putText(img, text, (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        #gives coordinates later used to figure out if a feature is existant.
        #  If a feature does not have all 4 elements, it is not complete
        coords = [x, y, w, h]
    return coords


#similar to previous function, only used to initilize previous face before figuring out if there is a mask or not.
def initial(img, classifier, scaleFactor, minNeighbors):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
    coords = []
    for (x, y, w, h) in features:
        coords = [x, y, w, h]
    return coords


# used to detect face,eyes,and mouths and uses to find if mask is on or not
def maskCheck(img, faceCascade, eyeCascade, mouthCascade):
    color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0), "white":(255,255,255)}
    #checks initially for the face
    coords = initial(img, faceCascade, 1.1, 10)
    #if a face exists, it looks for eyes and mouth
    if len(coords)==4:
        #limits the range of possible places for eyes and mouth to where the face was detected
        roi = img[coords[1]:coords[1]+coords[3], coords[0]:coords[0]+coords[2]]
        #if eyes are found, it labels them
        n = shape(roi, eyeCascade, 1.1, 12, color['white'], "Eye")

       #if mouth is found, it labels it  
        m = shape(roi, mouthCascade, 1.1, 20, color['white'], "Mouth")
        #if mouth isn't found, it assumes a mask is worn
        if len(m)!=4:
            shape(img, faceCascade, 1.1, 10, color['blue'], "Mask")
        #else assumes a mask is not warn
        else:
            shape(img, faceCascade, 1.1, 10, color['red'], "No mask")            
    return img


# classifiers
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eyesCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
mouthCascade = cv2.CascadeClassifier('Mouth.xml')

#Video Stream. If external camera, it would be -1
video_capture = cv2.VideoCapture(0)
#captures one image per 30 frames
video_capture.set(1,30)


while True:
    #getting a picture from the video to looks for face
    _,img = video_capture.read()
    img = maskCheck(img, faceCascade, eyesCascade, mouthCascade)
    # showing the image returned 
    cv2.imshow("face detection", img)
    #after 1 second, pressing q will terimate program
    if  cv2.waitKey(30) & 0xFF == ord('q'):
        break


video_capture.release()

cv2.destroyAllWindows()

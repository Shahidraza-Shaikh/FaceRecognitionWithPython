# Implementing Eye detection using frontal face & eye Cascade file With Python & OpenCV

import cv2

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')   #Enter the path of cascade file

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  #Enter the path of cascade file

# Getting the live camera to be accessed by the program
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read() #reading the frame 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converting the frame to grayscale frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w] #getting the face area with frontal face cascade file
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        # Plotting eye with eye cascade on face area 
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    if cv2.waitKey(2) & 0xFF == ord('e'): break

cv2.destroyAllWindows()
cap.release()

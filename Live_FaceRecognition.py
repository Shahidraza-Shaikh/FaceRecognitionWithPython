import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video = cv2.VideoCapture(0)
print(type(video))
print(video)
while True:
    check,frames = video.read()
    print(frames)
    gray = cv2.cvtColor(frames ,cv2.COLOR_BGR2GRAY)
    faces =face_cascade.detectMultiScale(gray ,scaleFactor=1.3,minNeighbors=1)
    for x,y,w,h in faces:
        img = cv2.rectangle(frames, (x,y), (x+w ,y+h), (0,255,0), 3)
    cv2.imshow('video',frames)
    cv2.waitKey(2)
cv2.destroyAllWindows()
video.release() 
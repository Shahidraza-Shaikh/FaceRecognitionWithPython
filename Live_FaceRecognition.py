# Python Program to Detect the Face of Human with openCV & Frontal Face cascade xml File
# ---- Input taken is Either a Path of a Recorded Video OR Accessing a WebCam ---- 


# Importing openCV Module
import cv2

# Accessing the frontalface cascade xml file with cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Taking the video Option from user as an input 
video_input = int(input("Choose the Preferred Option:\n 1. For Recorded Video\n 2. For Accessing WebCam\n---> "))

flag = True   # for Error Handling

if video_input == 1:
    path = input("Enter the Path for the Recorded Video\n---> ")   
    video = cv2.VideoCapture(path) 

    # loop is not going to terminate until video gets end or user press 'x' key
    while video.isOpened():
        check,frames = video.read()   # Reading the Video frame by frame from the recorded video
        gray = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)    # converting the colourful image to grayscale
        faces = face_cascade.detectMultiScale(gray ,scaleFactor=1.3,minNeighbors=1)    # Embedding features of cascadefile in frames
        for x,y,w,h in faces:
            img = cv2.rectangle(frames, (x,y), (x+w ,y+h), (0,255,0), 3)     # detecting faces in a video in a rectangle shape
        cv2.imshow('video',frames)    # plotting frame by frame
        if cv2.waitKey(1) & 0xFF == ord('x'): break    #condition to break the video streaming in between

elif video_input == 2:
    video = video = cv2.VideoCapture(0)

    # loop is not going to terminate until user press 'x' key
    while True: 
        check,frames = video.read()
        gray = cv2.cvtColor(frames ,cv2.COLOR_BGR2GRAY)
        faces =face_cascade.detectMultiScale(gray ,scaleFactor=1.3,minNeighbors=1)
        for x,y,w,h in faces:
            img = cv2.rectangle(frames, (x,y), (x+w ,y+h), (0,255,0), 3)
        cv2.imshow('video',frames)
        if cv2.waitKey(1) & 0xFF == ord('x'): break

else:
    print("Enter the Correct Option :)")
    flag = False


if flag:
    cv2.destroyAllWindows()   # Closing all the open windows which are processing video
    video.release()   # Closing the Video 
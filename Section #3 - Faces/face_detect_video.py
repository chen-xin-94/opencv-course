import cv2 as cv
import time

capture = cv.VideoCapture('Resources/Videos/faces.mp4')

# used to record the time when we processed last frame
prev_frame_time = 0

# used to record the time at which we processed current frame
new_frame_time = 0


# font which we will be using to display FPS
font = cv.FONT_HERSHEY_SIMPLEX

while True:
    isTrue, frame = capture.read()
    if isTrue:
        cv.imshow('Original Video', frame)

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        haar_cascade = cv.CascadeClassifier('./Section #3 - Faces/haar_face.xml')
        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

        # print(f'Number of faces found = {len(faces_rect)}')

        for (x,y,w,h) in faces_rect:
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

        # cv.imshow('Video with Detected Faces', frame)

        # time when we finish processing for this frame
        new_frame_time = time.time()
    
        # Calculating the fps
    
        # fps will be number of frame processed in given time frame
        # since their will be most of time error of 0.001 second
        # we will be subtracting it to get more accurate result
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time

        # converting the fps into integer
        fps = int(fps)
    
        # converting the fps to string so that we can display it on frame
        # by using putText function
        fps = str(fps)
    
        # putting the FPS count on the frame
        cv.putText(frame, fps, (7, 70), font, 3, (100, 255, 0), 3, cv.LINE_AA)

        cv.imshow('Original Video with detected Faces and FPS', frame)


        if cv.waitKey(20) & 0xFF == ord('q'):
            break
    else: 
        break

capture.release()
cv.destroyAllWindows()
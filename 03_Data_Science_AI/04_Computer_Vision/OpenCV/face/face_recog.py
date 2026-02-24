import cv2

#haar cascade - ml-based obj detection using opencv 

#detections:
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(1) # capture frames from a camera; 0 = default webcam

#loop runs if capturing has been init
while 1:
    ret, img = cap.read() #reads frames from cam
    if not ret:  # check if frame is captured
        print("Failed to grab frame")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to gray scale/bw; since comps. process black-and-white faster than full color

    faces = face.detectMultiScale(gray, 1.3,5) #scan the image at different sizes and find faces

    #draw rectangles during face detection
    for (x,y,w,h) in faces:
        #draw rectangle around 
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

        reg_of_interest_gray = gray[y:y+h, x:x+w] #get face area for grayscale
        reg_of_interest_color = img[y:y+h, x:x+w] #get face area from orig color 

        eyes = eye.detectMultiScale(reg_of_interest_gray)  #detects eyes
        for (a,b,c,d) in eyes: 
           cv2.rectangle(reg_of_interest_color, (a,b), (a+c, b+d), (230, 224, 176), 2)

    cv2.imshow("Your Face", img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release() #close window
cv2.destroyAllWindows() 

###pres ESC to close web cam
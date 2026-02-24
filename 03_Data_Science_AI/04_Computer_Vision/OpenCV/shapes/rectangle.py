import numpy as np
import cv2

img = np.zeros((400,400,3), dtype="uint8") #np.zeros() arr of zeroes; (h,w,color channel)

#create rectangle shape
cv2.rectangle(img, (30, 30), (300, 200), (0, 255, 0), 5) #top l, bot r, colors in bgr: green color; 5  is thickness

cv2.imshow('Rectangle', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
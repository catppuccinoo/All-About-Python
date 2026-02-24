import cv2

#imgread func
img = cv2.imread("sample_img_guide.png", cv2.IMREAD_COLOR)

cv2.imshow("Gudetama", img); #displays img in a window

filename ="coolkog_gudetama.png"

cv2.imwrite(filename, img) #save image @local

cv2.waitKey(0) #waits till a key is pressed; needed or window will close immediately

cv2.destroyAllWindows(); #closes after key press

print (img)

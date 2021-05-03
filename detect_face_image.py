#Programmed by Shounak Chandra
#Hooghly Engineering & Technology College
#Use only image
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


img = cv2.imread('test.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, 1.1, 4)


for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    if __name__ == '__main__':
    	main(h,x,y)
    	(255,0,1)0


cv2.imshow('img', img)
cv2.waitKey()

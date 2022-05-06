import cv2


#Explore OpenCV library on an image
img = cv2.imread("galaxy.jpg", 0)

print(img)
print(img.shape)
print(img.ndim)

img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Galaxy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#Explore OpenCV library on multiple images 
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(1000,1000))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)
    


#Detect faces in an image
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("news.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
                                    scaleFactor = 1.15,
                                    minNeighbors = 5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)

print(type(faces))
print(faces)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Exploreing video processing 
video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    print(check)
    print(frame)
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    
video.release()
cv2.destroyAllWindows()






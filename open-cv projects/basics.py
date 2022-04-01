
import cv2,time
'''face_cascade = cv2.CascadeClassifier("E:\projects\open-cv projects\haarcascade_frontalface_default.xml")
img = cv2.imread("E:\projects\open-cv projects\kiran.jpg",1)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img,scaleFactor = 1.05, minNeighbors = 5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("kiran",img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


'''video = cv2.VideoCapture(0)
check,frame = video.read()
print(check)
print(frame)
time.sleep(3)
cv2.imshow("capturing",frame)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()'''

face_cascade = cv2.CascadeClassifier("E:\projects\open-cv projects\haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)
a=1
while True:
    a=a+1
    check,frame = video.read()
    print(frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor = 1.05, minNeighbors = 5)
    for x,y,w,h in faces:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.imshow("capturing",img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
print(a)
video.release()
cv2.destroyAllWindows


import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd="E:\\projects\\t\\tesseract.exe"





url = 'http://192.168.0.5:8080/video'
cap = cv2.VideoCapture(url)
while(True):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame',frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break

    
    
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img))
cv2.destroyAllWindows()



    
    
from operator import truediv
from sre_constants import SUCCESS
import cv2 as cv
import numpy as np
from pyzbar.pyzbar import decode

#img = cv.imread('E:\projects\open-cv projects\qrcode.png')
cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,680)
with open('E:\projects\open-cv projects\mydata.txt') as f:
    mydatalist = f.read().splitlines()

while True:
    SUCCESS, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)
        if myData in mydatalist:
            myOutput ='Authorized'
            myColor = (0,255,0)
        else:
            myOutput ='Un-Authorized'
            myColor = (0,0,255)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv.polylines(img,[pts],True,myColor,3)
        pts2 = barcode.rect
        cv.putText(img,myOutput,(pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)
    cv.imshow('RESULT',img)
    cv.waitKey(1)


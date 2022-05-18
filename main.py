import cv2
import os
import numpy as np
from ocr import max_temp
from time import sleep
cap = cv2.VideoCapture("/dev/video3")
sleep(1)
while(1) :
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    cv2.imshow('frame', frame)

    print(max_temp(frame))
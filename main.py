# import dependecies
import mediapipe as mp
import cv2
import numpy as np
import os

# settng up hand model and stuff to draw the joints
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hand #hand model

# init the webcam

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow('hand tracking', frame)

    #quit using q btn

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
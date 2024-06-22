# import dependecies
import mediapipe as mp
import cv2
import numpy as np
import os

# settng up hand model and stuff to draw the joints
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands #hand model

# init the webcam

cap = cv2.VideoCapture(0)
#set confidence level stuff loop
with mp.hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: #detect hand at 80% and tracking at 50%
    while cap.isOpened():
        ret, frame = cap.read()

        #detecttions
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)


        cv2.imshow('hand tracking', frame)

        #quit using q btn
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
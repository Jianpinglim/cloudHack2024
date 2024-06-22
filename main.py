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
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: #detect hand at 80% and tracking at 50%
    while cap.isOpened():
        ret, frame = cap.read()

        #detecttions
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        #time to render the joints!
        #check if theres any landmarks
        if results.multi_hand_landmarks: 
            for num, hand in enumerate(results.multi_hand_landmarks): 
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, mp_drawing.DrawingSpec(color=(121, 22, 76), thickness = 2, circle_radius = 4), mp_drawing.DrawingSpec(color=(121, 44, 250), thickness = 2, circle_radius = 2))


        cv2.imshow('hand tracking', image)

        #quit using q btn
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
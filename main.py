# import dependecies
import mediapipe as mp
import cv2
import numpy as np
import os
from playsound import playsound as ps
import threading

# settng up hand model and stuff to draw the joints
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands #hand model

#create a touch threshold for how far the finger can be considered as touching
touchThreshold = 0.05 #change to suit later
#we create a function for calculating the distance

def calDist(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

#play the sound in a diff function, thread
def playSound(file):
    ps(file)

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
                landMarks = hand.landmark #extract the coords and put in a variable

                #since we tracking the thumb connection to other finger landmark of thumb is 4 0 is wrist

                thumbTip = (landMarks[4].x, landMarks[4].y)

                #we check which one touch the thumb in a dict

                touches = {}

                #init the fingertips and landmarks in a list

                fingertips = [8, 12, 16, 20]
                fingerNames = ['IndexFinger', 'MiddleFinger', 'RingFinger', 'PinkyFinger']

                for i, tip in enumerate(fingertips):
                    finger_tip = (landMarks[tip].x, landMarks[tip].y)
                    dist = calDist(thumbTip, finger_tip)
                    if dist < touchThreshold:
                        touches[fingerNames[i]] = True
                    else:
                        touches[fingerNames[i]] = False

                handedness = results.multi_handedness[num].classification[0]   .label

                #bruh is there no switch statements in python huh
                for finger, is_touching in touches.items():
                    if is_touching:
                        sound_file = ''
                        if finger == 'IndexFinger':
                            sound_file = 'piano-c_C_major.wav'

                        elif finger == 'MiddleFinger':
                            sound_file = 'piano-g_G_major.wav'

                        elif finger == 'RingFinger':
                            sound_file = 'piano-f_F_major.wav'

                        elif finger == 'PinkyFinger':
                            sound_file = 'piano-d_D_major.wav'
                        
                        if sound_file:
                            threading.Thread(target=playSound, args=(sound_file,)).start() #ty chatgpt

                        print(f"{handedness} hand {finger} is touching the thumb.")
                #loop thru the fingertios and see which one touch
        cv2.imshow('piano sellers go bye bye', image)

        #quit using q btn
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
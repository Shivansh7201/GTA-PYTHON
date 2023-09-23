import numpy as np
import mediapipe as mp
import cv2
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.4,
    min_tracking_confidence=0.4) as hands:

    while cap.isOpened():

        success, image = cap.read()

        h, w, c = image.shape

        start = time.perf_counter()


        image= cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

        image.flags.writeable = False

        results = hands.process(image)

        image.flags.writeable = True

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
    
               mp_drawing.draw_landmarks(
                    image,hand_landmarks,mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),
               mp_drawing_styles.get_default_hand_connections_style())


               index_finger_tip = hand_landmarks.landmark[0]

               index_finger_tip_x = index_finger_tip.x * w
               index_finger_tip_y = index_finger_tip.y * h

               if index_finger_tip_x > w/2:
                   cv2.putText(image, "RIGHT", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                   pyautogui.press('right')
                   pyautogui.pree('left')
               elif index_finger_tip_x < w/2:
                   cv2.putText(image, "LEFT", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                   pyautogui.press('left')
                   pyautogui.press('right')
               break
            

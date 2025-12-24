import cv2
import numpy as np


BASELINE_CM = 12.0       
FOCAL_LENGTH_PX = 700   
GREEN_LOWER = np.array([40, 70, 70])
GREEN_UPPER = np.array([80, 255, 255])
 

def detect_green_x(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, GREEN_LOWER, GREEN_UPPER)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        c = max(contours, key=cv2.contourArea)
        if cv2.contourArea(c) > 500:
            x, y, w, h = cv2.boundingRect(c)
            cx = x + w // 2
            cy = y + h // 2
            cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
            return cx, frame

    return None, frame


cap_left = cv2.VideoCapture(0)
cap_right = cv2.VideoCapture(1)

if not cap_left.isOpened() or not cap_right.isOpened():
    print("Camera not detected")
    exit()

while True:
    retL, frameL = cap_left.read()
    retR, frameR = cap_right.read()

    if not retL or not retR:
        break

    xL, frameL = detect_green_x(frameL)
    xR, frameR = detect_green_x(frameR)

    if xL is not None and xR is not None:
        disparity = abs(xL - xR)

        if disparity > 0:
            distance_cm = (FOCAL_LENGTH_PX * BASELINE_CM) / disparity
            cv2.putText(frameL, f"Distance: {distance_cm:.1f} cm",
                        (30, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

    cv2.imshow("Left Camera", frameL)
    cv2.imshow("Right Camera", frameR)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_left.release()
cap_right.release()
cv2.destroyAllWindows()

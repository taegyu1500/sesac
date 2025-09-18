import cv2
import numpy as np

cap = cv2.VideoCapture(0)
topleft = (50, 50)
bottomright = (300, 300)



while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break


    cv2.line(frame, topleft, bottomright, (0,255,0), 5)
    cv2.rectangle(frame, [pt+30 for pt in topleft], [pt-30 for pt in bottomright], (0,0,255), 5)
    cv2.circle(frame, (200,200), 50, (255,0,0), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "me", [pt+80 for pt in topleft], font, 2, (0,255,255), 10)
    cv2.imshow('Camera', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


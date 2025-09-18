import cv2
import functools
import numpy as np
from util import draw_shadow_text
import sys

def nothing(x):
    pass

WINDOW_NAME = 'LAB color'
TB_LIGHT_MIN = 'L_min'
TB_A_MIN = 'A_min'
TB_B_MIN = 'B_min'
TB_LIGHT_MAX = 'L_max'
TB_A_MAX = 'A_max'
TB_B_MAX = 'B_max'

l_min_value = 0
a_min_value = 0
b_min_value = 0
l_max_value = 255
a_max_value = 255
b_max_value = 255

def update_color_value(x, color, is_min):
    global l_min_value, a_min_value, b_min_value, l_max_value, a_max_value, b_max_value
    print(f"{color} value: {x}, is_min: {is_min}")
    if color == "L":
        if is_min:
            l_min_value = x
        else:
            l_max_value = x
    elif color == "A":
        if is_min:
            a_min_value = x
        else:
            a_max_value = x
    elif color == "B":
        if is_min:
            b_min_value = x
        else:
            b_max_value = x

        
cv2.namedWindow(WINDOW_NAME)
cv2.createTrackbar(TB_LIGHT_MIN, WINDOW_NAME, l_min_value, 255, functools.partial(update_color_value, color="L", is_min=True))
cv2.createTrackbar(TB_LIGHT_MAX, WINDOW_NAME, l_max_value, 255, functools.partial(update_color_value, color="L", is_min=False))
cv2.createTrackbar(TB_A_MIN, WINDOW_NAME, a_min_value, 255, functools.partial(update_color_value, color="A", is_min=True))
cv2.createTrackbar(TB_A_MAX, WINDOW_NAME, a_max_value, 255, functools.partial(update_color_value, color="A", is_min=False))
cv2.createTrackbar(TB_B_MIN, WINDOW_NAME, b_min_value, 255, functools.partial(update_color_value, color="B", is_min=True))
cv2.createTrackbar(TB_B_MAX, WINDOW_NAME, b_max_value, 255, functools.partial(update_color_value, color="B", is_min=False))

cap = cv2.VideoCapture(0)

while True:
    # Filter in LAB space
    cap.read()
    ret, img = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    lower = np.array([l_min_value, a_min_value, b_min_value])
    upper = np.array([l_max_value, a_max_value, b_max_value])
    mask = cv2.inRange(lab, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    result_open = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    result_close = cv2.bitwise_and(img, img, mask=mask)

    combined = np.hstack((img, result_open, result_close))
    cv2.imshow(WINDOW_NAME, cv2.resize(combined, (1280, 720)))
    
    if(cv2.waitKey(1) & 0xFF) == 27:
        break
    
    

cv2.destroyAllWindows()
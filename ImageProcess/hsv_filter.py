import cv2
import functools
import numpy as np
from util import draw_shadow_text
import sys


def nothing(x):
    pass

WINDOW_NAME = 'RGB color'
TB_HUE_MIN = 'H_min'
TB_SATURATION_MIN = 'S_min'
TB_VALUE_MIN = 'V_min'
TB_HUE_MAX = 'H_max'
TB_SATURATION_MAX = 'S_max'
TB_VALUE_MAX = 'V_max'

h_min_value = 0
s_min_value = 0
v_min_value = 0
h_max_value = 179
s_max_value = 255
v_max_value = 255

def update_color_value(x, color, is_min):
    global h_min_value, s_min_value, v_min_value, h_max_value, s_max_value, v_max_value
    print(f"{color} value: {x}, is_min: {is_min}")
    if color == "H":
        if is_min:
            h_min_value = x
        else:
            h_max_value = x
    elif color == "S":
        if is_min:
            s_min_value = x
        else:
            s_max_value = x
    elif color == "V":
        if is_min:
            v_min_value = x
        else:
            v_max_value = x

        
cv2.namedWindow(WINDOW_NAME)
cv2.createTrackbar(TB_HUE_MIN, WINDOW_NAME, 0, 179, functools.partial(update_color_value, color="H", is_min=True))
cv2.createTrackbar(TB_HUE_MAX, WINDOW_NAME, 0, 179, functools.partial(update_color_value, color="H", is_min=False))
cv2.createTrackbar(TB_SATURATION_MIN, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color="S", is_min=True))
cv2.createTrackbar(TB_SATURATION_MAX, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color="S", is_min=False))
cv2.createTrackbar(TB_VALUE_MIN, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color="V", is_min=True))
cv2.createTrackbar(TB_VALUE_MAX, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color="V", is_min=False))

img = cv2.imread(sys.argv[1]) if len(sys.argv) > 1 else cv2.imread("./data/a.jpg")

while True:
    # Filter in HSV space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([h_min_value, s_min_value, v_min_value])
    upper = np.array([h_max_value, s_max_value, v_max_value])
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(hsv, hsv, mask=mask)

    combined = np.hstack((img, cv2.cvtColor(result, cv2.COLOR_HSV2BGR)))
    cv2.imshow(WINDOW_NAME, cv2.resize(combined, (1280, 720)))
    
    if(cv2.waitKey(1) & 0xFF) == 27:
        break
    
    

cv2.destroyAllWindows()
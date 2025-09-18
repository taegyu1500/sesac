import cv2
import functools
import numpy as np
from util import draw_shadow_text
import sys


def nothing(x):
    pass

WINDOW_NAME = 'RGB color'
TB_RED_MIN = 'R_min'
TB_RED_MAX = 'R_max'
TB_GREEN_MIN = 'G_min'
TB_GREEN_MAX = 'G_max'
TB_BLUE_MIN = 'B_min'
TB_BLUE_MAX = 'B_max'

r_min_value = 0
g_min_value = 0
b_min_value = 0
r_max_value = 255
g_max_value = 255
b_max_value = 255

def update_color_value(x, color, is_min):
    global r_min_value, g_min_value, b_min_value, r_max_value, g_max_value, b_max_value
    print(f"{color} value: {x}, is_min: {is_min}")
    if color == "R":
        if is_min:
            r_min_value = x
        else:
            r_max_value = x
    elif color == "G":
        if is_min:
            g_min_value = x
        else:
            g_max_value = x
    elif color == "B":
        if is_min:
            b_min_value = x
        else:
            b_max_value = x

        
cv2.namedWindow(WINDOW_NAME)
cv2.createTrackbar(TB_RED_MIN, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color="R", is_min=True))
cv2.createTrackbar(TB_RED_MAX, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color="R", is_min=False))
cv2.createTrackbar(TB_GREEN_MIN, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color="G", is_min=True))
cv2.createTrackbar(TB_GREEN_MAX, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color="G", is_min=False))
cv2.createTrackbar(TB_BLUE_MIN, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color="B", is_min=True))
cv2.createTrackbar(TB_BLUE_MAX, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color="B", is_min=False))

img = cv2.imread(sys.argv[1]) if len(sys.argv) > 1 else cv2.imread("./data/a.jpg")

while True:
    # Filter in RGB space
    lower = np.array([b_min_value, g_min_value, r_min_value])
    upper = np.array([b_max_value, g_max_value, r_max_value])
    mask = cv2.inRange(img, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    combined = np.hstack((img, result))
    cv2.imshow(WINDOW_NAME, cv2.resize(combined, (1280, 720)))
    
    if(cv2.waitKey(1) & 0xFF) == 27:
        break
    
    

cv2.destroyAllWindows()
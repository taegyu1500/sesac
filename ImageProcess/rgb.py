import cv2
import functools
import numpy as np
from util import draw_shadow_text

def nothing(x):
    pass

WINDOW_NAME = 'RGB color'
TB_RED = 'R'
TB_GREEN = 'G'
TB_BLUE = 'B'

red_value = 0
green_value = 0
blue_value = 0

def update_color_value(x, color):
    global red_value, green_value, blue_value
    print(f"{color} value: {x}")
    if color == TB_RED:
        red_value = x
    elif color == TB_GREEN:
        green_value = x
    elif color == TB_BLUE:
        blue_value = x

cv2.namedWindow(WINDOW_NAME)
cv2.createTrackbar(TB_RED, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color=TB_RED))
cv2.createTrackbar(TB_GREEN, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color=TB_GREEN))
cv2.createTrackbar(TB_BLUE, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color=TB_BLUE))

img = np.zeros((200, 800,3), dtype=np.uint8)
while True:
    img[:] = [blue_value, green_value, red_value]
    draw_shadow_text(img, 10, 30, f"R: {red_value}, G: {green_value}, B: {blue_value}")
    
    cv2.imshow(WINDOW_NAME, img)
    if(cv2.waitKey(1) & 0xFF) == 27:
        break
    
    

cv2.destroyAllWindows()
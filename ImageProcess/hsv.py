import cv2
import functools
import numpy as np
from util import draw_shadow_text

def nothing(x):
    pass

WINDOW_NAME = 'HSV color'
TB_HUE = 'H'
TB_SATURATION = 'S'
TB_VALUE = 'V'

hue_value = 0
saturation_value = 0
value_value = 0

def update_color_value(x, color):
    global hue_value, saturation_value, value_value
    print(f"{color} value: {x}")
    if color == TB_HUE:
        hue_value = x
    elif color == TB_SATURATION:
        saturation_value = x
    elif color == TB_VALUE:
        value_value = x

cv2.namedWindow(WINDOW_NAME)
cv2.createTrackbar(TB_HUE, WINDOW_NAME, 0, 179, functools.partial(update_color_value, color=TB_HUE))
cv2.createTrackbar(TB_SATURATION, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color=TB_SATURATION))
cv2.createTrackbar(TB_VALUE, WINDOW_NAME, 0, 255, functools.partial(update_color_value, color=TB_VALUE))

img = np.zeros((200, 800,3), dtype=np.uint8)
while True:
    # Convert HSV to BGR for display
    # img[:] = [value_value, saturation_value, hue_value]
    hsv_color = np.uint8([[[hue_value, saturation_value, value_value]]])
    b,g,r = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2BGR)[0][0]
    img[:] = [b, g, r]
    draw_shadow_text(img, 10, 30, f"H: {hue_value}, S: {saturation_value}, V: {value_value}")
    draw_shadow_text(img, 10, 70, f"R: {r}, G: {g}, B: {b}")
    
    cv2.imshow(WINDOW_NAME, img)
    if(cv2.waitKey(1) & 0xFF) == 27:
        break
    
    

cv2.destroyAllWindows()
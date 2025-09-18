import cv2
import functools
import numpy as np
import os

def nothing(x):
    pass

WINDOW_NAME = 'HSV color'
TB_HUE = 'H'
TB_SATURATION = 'S'
TB_VALUE = 'V'
IMAGE_PATH = os.path.abspath("./data/e.jpg")

hue_value = 0
saturation_value = 125 
value_value = 125

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
cv2.setTrackbarPos(TB_HUE, WINDOW_NAME, hue_value)
cv2.setTrackbarPos(TB_SATURATION, WINDOW_NAME, saturation_value)
cv2.setTrackbarPos(TB_VALUE, WINDOW_NAME, value_value)


og_img = cv2.imread(IMAGE_PATH)
if og_img is None:
    print(f"이미지를 불러오지 못했습니다. 경로: {IMAGE_PATH}")
    print("파일 존재 여부:", os.path.exists(IMAGE_PATH))
    raise SystemExit(1)
img = og_img.copy()

while True:
    # Convert HSV to BGR for display
    # img[:] = [value_value, saturation_value, hue_value]
    hsv_img = cv2.cvtColor(og_img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_img)
    
    h_new = (h + hue_value) % 179
    s_new = np.clip(s.astype(np.int16) + saturation_value - 125, 0, 255)
    v_new = np.clip(v.astype(np.int16) + value_value - 125, 0, 255)
    
    hsv_modified = cv2.merge([h_new.astype(np.uint8), s_new.astype(np.uint8), v_new.astype(np.uint8)])
    
    bgr_modified = cv2.cvtColor(hsv_modified, cv2.COLOR_HSV2BGR)
    img[:] = bgr_modified

    cv2.imshow(WINDOW_NAME, img)
    if(cv2.waitKey(1) & 0xFF) == 27:
        break
    
cv2.destroyAllWindows()
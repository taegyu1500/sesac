import cv2
import functools
import numpy as np
import json
import os

WINDOW_NAME = 'LAB color'
TB_LIGHT_MIN = 'L_min'
TB_A_MIN = 'A_min'
TB_B_MIN = 'B_min'
TB_LIGHT_MAX = 'L_max'
TB_A_MAX = 'A_max'
TB_B_MAX = 'B_max'

CFG_PATH = 'LAB_calib.json'
DEFAULT_CFG = {
    TB_LIGHT_MIN: 0, TB_A_MIN: 0, TB_B_MIN: 0,
    TB_LIGHT_MAX: 255, TB_A_MAX: 255, TB_B_MAX: 255
}

def load_config(path=CFG_PATH):
    if os.path.exists(path):
        try:
            with open(path, 'r') as f:
                data = json.load(f)
                return {k: int(data.get(k, DEFAULT_CFG[k])) for k in DEFAULT_CFG}
        except Exception:
            pass
    return DEFAULT_CFG.copy()

def save_config(cfg, path=CFG_PATH):
    with open(path, 'w') as f:
        json.dump(cfg, f, indent=4)
    print(f"Calibration data saved to {path}")

def on_trackbar(val, cfg, key):
    cfg[key] = val

def create_trackbars(cfg):
    cv2.namedWindow(WINDOW_NAME)
    # 트랙바 정의: (key, max)
    bars = [
        (TB_LIGHT_MIN, 255), (TB_LIGHT_MAX, 255),
        (TB_A_MIN, 255), (TB_A_MAX, 255),
        (TB_B_MIN, 255), (TB_B_MAX, 255),
    ]
    for key, mx in bars:
        cv2.createTrackbar(key, WINDOW_NAME, cfg[key], mx, functools.partial(on_trackbar, cfg=cfg, key=key))
        cv2.setTrackbarPos(key, WINDOW_NAME, cfg[key])

def process_frame(img, cfg):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    lower = np.array([cfg[TB_LIGHT_MIN], cfg[TB_A_MIN], cfg[TB_B_MIN]])
    upper = np.array([cfg[TB_LIGHT_MAX], cfg[TB_A_MAX], cfg[TB_B_MAX]])
    mask = cv2.inRange(lab, lower, upper)
    kernel = np.ones((5,5), np.uint8)

    mask_open = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask_close = cv2.morphologyEx(mask_open, cv2.MORPH_CLOSE, kernel)

    result_open = cv2.bitwise_and(img, img, mask=mask_open)
    result_close = cv2.bitwise_and(img, img, mask=mask_close)

    combined = np.hstack((img, result_open, result_close))
    return cv2.resize(combined, (1280, 720))

def main():
    cfg = load_config()
    create_trackbars(cfg)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
        return

    try:
        while True:
            ret, img = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            display = process_frame(img, cfg)
            cv2.imshow(WINDOW_NAME, display)

            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC
                break
            if key == ord('s'):
                save_config(cfg)
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
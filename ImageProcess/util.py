import cv2

def draw_shadow_text(img, x, y, text):
    """이미지 위에 그림자 텍스트를 그립니다.
    Args:
        img (_type_): 그릴 이미지
        x (_type_): 텍스트의 x 좌표
        y (_type_): 텍스트의 y 좌표
        text (_type_): 그릴 텍스트
    """
    cv2.putText(img, text, (x+1, y+1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
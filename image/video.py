import cv2

cap = cv2.VideoCapture("ronaldinho.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS: {fps}")
if fps == 0:
    fps = 30  # 기본 FPS 설정
delay = int(1000 / fps)
captured_frame = 0 

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        # 영상이 끝나면 루프가 종료되고 있지만 처음으로 돌아가게 하기
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
    
    # 영상 크기 조절
    h, w = frame.shape[:2]
    frame = cv2.resize(frame, (w//2, h//2))
    cv2.imshow('frame', frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('c'):
        # 'c' 키를 누르면 현재 프레임을 이미지로 저장
        cv2.imwrite(f'captured_frame_{captured_frame}.jpg', frame)
        captured_frame += 1

cap.release()
cv2.destroyAllWindows()
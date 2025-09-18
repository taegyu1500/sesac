import cv2
import os
cap = cv2.VideoCapture(0)

w = 640 # 1280
h = 480 # 720

cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# output.mp4 이미 있으면
if os.path.exists('output.mp4'):
    os.remove('output.mp4')
writer = cv2.VideoWriter('output.mp4', fourcc, 30, (w, h))
flag = False

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('frame', frame)
    if(writer is not None):
        writer.write(frame)
    key = cv2.waitKey(1) & 0xFF
    
    

    if key == ord('q'):
        break
    elif key == ord('r'):
        # 'r'키 누르면 녹화 시작, 다시 'r'키 누르면 녹화 중지
        if not flag:
            print("녹화 시작")
            writer = cv2.VideoWriter('output.mp4', fourcc, 30, (w, h))
            flag = True
        else:
            print("녹화 종료")
            writer.release()
            writer = None
            flag = False

cap.release()
cv2.destroyAllWindows()
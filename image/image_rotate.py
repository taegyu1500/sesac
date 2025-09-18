import cv2

img = cv2.imread('my_input.jpg')

rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("original", img)
cv2.imshow("rotated", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
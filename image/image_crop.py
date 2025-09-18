import cv2

img = cv2.imread('my_input.jpg')    

cropped = img[50:450, 100:400]
resized = cv2.resize(cropped, (400,200))

cv2.imshow("original", img)
cv2.imshow("cropped", cropped)
cv2.imshow("resized", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
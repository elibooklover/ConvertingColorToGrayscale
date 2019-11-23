import cv2

image = cv2.imread('image1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('image1_gray.jpg', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


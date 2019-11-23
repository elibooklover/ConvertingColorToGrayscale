import cv2

directory1 = r'resized/' # Source Folder
directory2 = r'gray/' # Destination Folder

image = cv2.imread(directory1+'image1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite(directory2+'image1_gray.png', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


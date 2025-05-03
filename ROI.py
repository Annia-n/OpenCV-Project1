import cv2
import numpy

image = cv2.imread("/Users/anya/Desktop/opencv-project/fruit.webp")


resized = cv2.resize(image, (500, 500))
cv2.imshow("Resized Image", resized)

roi = resized[100:200, 100:200]  
cv2.imshow("ROI", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
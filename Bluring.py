import cv2
import numpy

image = cv2.imread("/Users/anya/Desktop/opencv-project/fruit.webp")

gaussian = cv2.GaussianBlur(image, (5, 5), 0)

median = cv2.medianBlur(image, 5)

average = cv2.blur(image, (5, 5))

cv2.imshow("Original", image)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)
cv2.imshow("Average Blur", average)

cv2.waitKey(0)
cv2.destroyAllWindows()
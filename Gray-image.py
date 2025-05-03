import cv2
import numpy as np


fruit_image = cv2.imread("/Users/anya/Desktop/opencv-project/fruit.webp")

fruit_gray_image = cv2.cvtColor(fruit_image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Fruit", fruit_gray_image)
cv2.imshow("Color Fruit", fruit_image)

cv2.imwrite("Grayfruit.png", fruit_gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

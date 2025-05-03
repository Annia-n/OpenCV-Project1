import cv2
import numpy


img = cv2.imread("/Users/anya/Desktop/opencv-project/fruit.webp")
if img is None:
    print("❌ تصویر پیدا نشد. مسیر رو بررسی کن.")
else:
    cv2.imshow("fruit.webp", img)
    cv2.waitKey(0)
    

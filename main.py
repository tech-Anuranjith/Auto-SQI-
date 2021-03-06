import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('bolt.jpg', 0)
canny = cv2.Canny(img,100,200)
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelC = cv2.bitwise_or(sobelX,sobelY)
titles = ['original', 'canny', 'sobelX', 'sobelY','sobleC' ]
images=[img, canny, sobelX, sobelY, sobelC]
for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
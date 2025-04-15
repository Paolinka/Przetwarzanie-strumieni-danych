import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('duma.jpg', cv2.IMREAD_COLOR)

# Wyświetlanie przy pomocy OpenCV
cv2.imshow("image", img)
cv2.waitKey(0)

# Wyświetlanie przy pomocy matplotlib
plt.imshow(img)
plt.axis("off")

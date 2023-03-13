import cv2
import numpy as np
from matplotlib import pyplot as plt


# deNOISING

path = r'C:\Users\anosh\OneDrive\Desktop\pygame\python_learn\images\DSimages\Neuron.jpg'

img = cv2.imread(path, 0) #0- grayscale 1-original

edges = cv2.Canny(img,100,200)

cv2.imshow("Original",img)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
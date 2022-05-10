import cv2
import numpy as np
def sketch(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    img_gray_blur =
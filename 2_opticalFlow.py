import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("Car_traffic_g2_c18.mp4")

ret, frame1 = cap.read()
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255
print(frame1.shape)


plt.imshow(frame1)
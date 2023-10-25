import matplotlib.pyplot as plt
import numpy as np
import cv2
#trnslating matrix of HHS
#shifting by (100,50)
M = np.float32([[1, 0, 100], [0 , 1, 50]])
try:
    S1 = cv2.imread(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
    HHS_T = cv2.warpAffine(S1, M, (100, 50))
    cv2.imwrite("HHS_T.tiff", S1)
    plt.imshow(HHS_T)
    plt.title("Translated HHS")
    plt.show()
except IOError:
    print("error")

#trnslating matrix of HvS
try:
    S1 = cv2.imread(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
    HVS_T = cv2.warpAffine(S1, M, (100, 50))
    cv2.imwrite("HVS_T.tiff", S1)
    plt.imshow(HVS_T)
    plt.title("Translated HVS")
    plt.show()
except IOError:
    print("error")
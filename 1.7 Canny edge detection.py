import matplotlib.pyplot as plt

import cv2
#canny edge detection of HHQ
try:
    S1 = cv2.imread(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
    edges_HHS = cv2.Canny(S1, 15, 10)
    cv2.imwrite("Canny Edge of HHS.tiff", edges_HHS)
    plt.imshow(edges_HHS)
    plt.title("Canny Edge of HHS")
    plt.show()
except IOError:
    print("Error")

#canny edge detection of HVS
try:
    S2 = cv2.imread(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
    edges_HVS = cv2.Canny(S2, 15, 10)
    cv2.imwrite("Canny Edge of HVQ.tiff", edges_HVS)
    plt.imshow(edges_HVS)
    plt.title("Canny Edge of HVS")
    plt.show()
except IOError:
    print("Error")
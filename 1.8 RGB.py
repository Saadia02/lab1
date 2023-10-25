import matplotlib.pyplot as plt
import cv2

#RGB of HHS
S1 = cv2.imread(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
HHS_rgb =cv2.cvtColor(S1, cv2.COLOR_BGR2RGB)
plt.imshow(HHS_rgb)
plt.axis('off')
plt.title("RGB of HHS")
plt.show()

#RGB of HVS
S2 = cv2.imread(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
HVS_rgb =cv2.cvtColor(S2, cv2.COLOR_BGR2RGB)
plt.imshow(HVS_rgb)
plt.axis('off')
plt.title("RGB of HVS")
plt.show()
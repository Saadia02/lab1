from PIL import Image
import numpy as np


#open image
S1 = Image.open(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
S2 = Image.open(r"D:\image processing\myenv\Unzip files\HV-ALPSRP247640510-H2.2_UA.tif")


#HHS
#convert image to numpy array
HHS_array = np.array(S1)

#Calculate the image statistics
mean = np.mean(HHS_array)
std_dev = np.std(HHS_array)
min = np.min(HHS_array)
max = np.max(HHS_array)

#print
print("Statistics of HHQ")
print("Mean of HHS:", mean)
print("Standard Deviation of HHs:", std_dev)
print("Min of HHS:", min)
print("Max of HHS:", max)

width, height = S1.size
print("Widthof HHs:", width)
print("Height: of HHS", height)

#HVS
#convert image to numpy array
HVS_array = np.array(S1)

#Calculate the image statistics
mean = np.mean(HVS_array)
std_dev = np.std(HVS_array)
min = np.min(HVS_array)
max = np.max(HVS_array)

#print
print("\n Statistics of HHS")
print("Mean of HVS:", mean)
print("Standard Deviation of HVS:", std_dev)
print("Min of HVS:", min)
print("Max of HVS:", max)

width, height = S1.size
print("Widthof HVS:", width)
print("Height: of HVS", height)
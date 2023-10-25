import rasterio
import matplotlib.pyplot as plt

#Meta data about tiff image

S1 = rasterio.open(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
S2 = rasterio.open(r"D:\image processing\myenv\Unzip files\HV-ALPSRP247640510-H2.2_UA.tif")

#META DATA OF HHS
width = S1.width
height = S1.height
print("Size of HHS (Width x Height) is", width, 'x', height)


n_bands = S1.count
print("Number of Bands of HHS are: ", n_bands)

S1.width
S1.height
S1.count

plt.imshow(S1.read(1))
plt.show()
S1.close()

#META DATA OF HVS
width = S2.width
height = S2.height

print("Size of HVQ (Width x Height) is", width, 'x', height)
n_bands = S2.count
print("Number of Bands of HVS are: ", n_bands)

S2.width
S2.height
S2.count

plt.imshow(S2.read(1))
plt.show()
S2.close()
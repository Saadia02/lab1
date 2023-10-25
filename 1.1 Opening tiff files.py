from rasterio.plot import show
from PIL import Image


# reading tiff file
S1 = Image.open(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
S2 = Image.open(r"D:\image processing\myenv\Unzip files\HV-ALPSRP247640510-H2.2_UA.tif")
show(S1)
pixels = S1.load()
show(S2)
pixels = S2.load()
import cv2
import matplotlib.pyplot as plt

try:
    # Read image from disk.
    S1 = cv2.imread(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
 
     # Shape of image in terms of pixels.
    (rows, cols) = S1.shape[:2]
 
    # getRotationMatrix2D creates a matrix needed for transformation.
    # We want matrix for rotation w.r.t center to 45 degree without scaling.
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    R_HHS = cv2.warpAffine(S1, M, (cols, rows))
 
    # Write image back to disk.
    cv2.imwrite('result.tiff', R_HHS)
    plt.imshow(R_HHS)
    plt.title("Rotated HHS")
    plt.show()
 
except IOError:
    print('Error while reading files !!!')

try:
    # Read image from disk.
    S2 = cv2.imread(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
 
     # Shape of image in terms of pixels.
    (rows, cols) = S2.shape[:2]
 
    # getRotationMatrix2D creates a matrix needed for transformation.
    # We want matrix for rotation w.r.t center to 45 degree without scaling.
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
    R_HVS = cv2.warpAffine(S2, M, (cols, rows))
 
    # Write image back to disk.
    cv2.imwrite('result.tiff', R_HVS)
    plt.imshow(R_HVS)
    plt.title("Rotated HVS")
    plt.show()
 
except IOError:
    print('Error while reading files !!!')

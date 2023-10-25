import matplotlib.pyplot as plt
import cv2

#Reducing size of the image
try:
    #read image from disk
    S1 = cv2.imread(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")
    #get no of pixel horizontally and vertically
    (height, width) = S1.shape[:2]

     # Specify the size of image along with interpolation methods.
    # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC is used for zooming.
    rsize_HHS = cv2.resize(S1, (int(width/2), int(height/2)), interpolation = cv2.INTER_CUBIC)

    #write the image back to disk
    cv2.imwrite("HHS resized.tiff", rsize_HHS)
    plt.imshow(rsize_HHS)
    plt.title("HHS Resized")
    plt.show()
except IOError:
    print("Error while reading tiff file!!!")

#Resizing HHV
try:
    #read image from disk
    S2 = cv2.imread(r"D:\image processing\myenv\Unzip files\HH-ALPSRP247640510-H2.2_UA.tif")

    #get no of pixel horizontally and vertically
    (height, width) = S2.shape[:2]

     # Specify the size of image along with interpolation methods.
    # cv2.INTER_AREA is used for shrinking, whereas cv2.INTER_CUBIC is used for zooming.
    rsize_HVS = cv2.resize(S2, (int(width/2), int(height/2)), interpolation = cv2.INTER_CUBIC)

    #write the image back to disk
    cv2.imwrite("HVS resized.tiff", rsize_HVS)
    plt.imshow(rsize_HVS)
    plt.title("HVS Resized")
    plt.show()
except IOError:
    print("Error while reading tiff file!!!")
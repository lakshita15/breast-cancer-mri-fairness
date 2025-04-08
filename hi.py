import SimpleITK as sitk

import matplotlib.pyplot as plt
import numpy as np

image = sitk.ReadImage('breast-cancer-mri-fairness/Data/PKG - Duke-Breast-Cancer-MRI-Supplement-v3/Duke-Breast-Cancer-MRI-Supplement-v3/Segmentation_Masks_NRRD/Breast_MRI_006/Segmentation_Breast_MRI_006_Breast.seg.nrrd')


image_array = sitk.GetArrayFromImage(image)

print(f"Array shape: {image_array.shape}") # Check the shape
num_components = image.GetNumberOfComponentsPerPixel()
print(f"Number of components per pixel: {num_components}")

if num_components == 3:
    # If components are the first dimension, transpose for matplotlib
    if image_array.shape[0] == 3:
        image_array = np.transpose(image_array, (1, 2, 0))
    plt.imshow(image_array)
    plt.title("Color Image")
    plt.show()
elif num_components == 4:
    # If components are the first dimension, transpose for matplotlib
    if image_array.shape[0] == 4:
        image_array = np.transpose(image_array, (1, 2, 0))
    plt.imshow(image_array)
    plt.title("RGBA Image")
    plt.show()
else:
    plt.imshow(image_array, cmap='gray') # Force grayscale colormap
    plt.title("Grayscale Image")
    plt.show()
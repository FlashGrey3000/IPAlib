import cv2
import numpy as np

def invert(img: np.ndarray) -> np.ndarray:
    """Inverts a given image"""
    return 255 - img                # applies 255 - [value] for each pixel

def threshold(img: np.ndarray, threshold: int) -> np.ndarray:
    """Displays pixels only above a particular intensity level - `threshold`  
    - `threshold`: should be an integer between (0-255)  

    Note: if the input `img` is not grayscale *(cv2.IMREAD_GRAYSCALE)* then each channel value will be thresholded,
    i.e. if `blue < threshold` then value for that pixel in the blue channel would be set to 0.
    *which might not be your desired result*"""

    if len(img.shape) > 2:
        print("Image is not grayscale, each channel value will be thresholded")
    
    return np.where(img > threshold, img, 0)

def threshold_binary(img: np.ndarray, threshold: int) -> np.ndarray:
    """If pixel value > `threshold` then set pixel value to 255 else 0"""

    if len(img.shape) > 2:
        print("Image is not grayscale, each channel value will be thresholded.\nUse cv2.IMREAD_GRAYSCALE while reading the image.")
    
    return np.where(img > threshold, 255, 0)


def correlate(img: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """Returns the correlation of `kernel` on `img`.  
    `kernel`: must be a **square matrix** with **odd** dimensions."""
    if kernel.shape[0] != kernel.shape[1]:
        raise ValueError(f"kernel MUST be a square matrix. Kernel shape: {kernel.shape}")
    if kernel.shape[0] % 2 == 0:
        raise ValueError(f"kernel MUST have odd dimensions. Kernel shape: {kernel.shape}")
    # its too much of a headache to consider the corners and edges.
    # On a later day, a pad() function can be created and include the *edge* cases. (pun intended).

    is_bgr = False
    if img.ndim == 3 and img.shape[2] == 3: # if not cv2.IMREAD_GRAYSCALE image do correlation for each channel
        is_bgr = True


    # find the center, so that we can extract the region of interest around each pixel in the image
    kernel_center = kernel.shape[0] // 2
    result = np.zeros_like(img)

    if not is_bgr:
        for row_i in range(kernel_center, img.shape[0] - kernel_center):
            for col_i in range(kernel_center, img.shape[1] - kernel_center):
                region = img[row_i - kernel_center : row_i + kernel_center + 1, col_i - kernel_center: col_i + kernel_center + 1]
                if region.shape == kernel.shape:
                    result[row_i, col_i] = np.sum(region * kernel) // 9
    else:
        for row_i in range(kernel_center, img.shape[0] - kernel_center):
            for col_i in range(kernel_center, img.shape[1] - kernel_center):
                # extracting all three regions for each channel simultaneously. (saves a lot of time)
                region1 = img[row_i - kernel_center : row_i + kernel_center + 1, col_i - kernel_center: col_i + kernel_center + 1, 0]
                region2 = img[row_i - kernel_center : row_i + kernel_center + 1, col_i - kernel_center: col_i + kernel_center + 1, 1]
                region3 = img[row_i - kernel_center : row_i + kernel_center + 1, col_i - kernel_center: col_i + kernel_center + 1, 2]
                result[row_i, col_i, 0] = np.sum(region1 * kernel) // 9
                result[row_i, col_i, 1] = np.sum(region2 * kernel) // 9
                result[row_i, col_i, 2] = np.sum(region3 * kernel) // 9
    
    return result

def convolution(img: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """Returns the convolution of `kernel` on `img`.  
    `kernel`: Must be a **square matrix** with **odd** dimensions"""
    
    return correlate(img, kernel.T) # Convolution is just the correlation with the transposed matrix
                    



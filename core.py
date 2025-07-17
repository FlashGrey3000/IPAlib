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

    if len(img.shape[2]) > 2:
        print("Image is not grayscale, each channel value will be thresholded")
    
    return np.where(img > threshold, img, 0)


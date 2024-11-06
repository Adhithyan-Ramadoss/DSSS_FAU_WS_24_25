"""
This script contains the methods to convert a given RGB image to greyscale using different conversion methodologies.
Author: Ramadoss, Adhithyan
06.11.2024
"""
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def load_image(image_path: str) -> np.ndarray:
    """
    Method to load an image from a given file path to an numpy array
    Args:
        image_path (str): File path to an image

    Returns:
        numpy array: the image loaded as numpy array

    Note: the input path must be an image file path.
    """
    image = Image.open(image_path)
    image_array = np.array(image)

    return image_array

def rgb_to_grayscale_lightness(image: np.ndarray) -> np.ndarray:
    """
    Conversion of RGB Image to Grayscale using the lightness method
    grayscale = (min(R,G,B) + max(R,G,B))/2
    Args:
        image (numpy array): Input RGB image

    Returns:
        numpy array: Grayscale image
    """
    grayscale = (np.min(image, axis=2) + np.max(image, axis=2))/2
    return grayscale

def rgb_to_grayscale_average(image: np.ndarray) -> np.ndarray:
    """
    Conversion of RGB Image to Grayscale using the average method
    grayscale = (R+G+B)/3
    Args:
        image (numpy array): Input RGB image

    Returns:
        numpy array: Grayscale image
    """
    grayscale_image = np.average(image, axis=2)  # average over the channel axis
    return grayscale_image


def rgb_to_grayscale_luminosity(image: np.ndarray) -> np.ndarray:
    """
    Conversion of RGB Image to Grayscale using the luminosity method
    grayscale = 0.2989 * R + 0.5870 * G + 0.1140 * B
    Args:
        image (numpy array): Input RGB image

    Returns:
        numpy array: Grayscale image
    """
    grayscale_image = 0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2]
    return grayscale_image

def plot_image(image: np.ndarray) -> None:
    """
    Collects thee grayscale images using different methods of a given RGB image and plots them
    Args:
        image (numpy array): Input RGB image

    Returns:
        None

    Requires:
        rgb_to_grayscale_average(),
        rgb_to_grayscale_luminosity(),
        rgb_to_grayscale_luminosity()
    """
    fig, axs = plt.subplots(1, 4, figsize=(8, 2.25), constrained_layout=True)

    images = [
        image,
        rgb_to_grayscale_average(image),
        rgb_to_grayscale_luminosity(image),
        rgb_to_grayscale_luminosity(image)
    ]
    plt_titles = ["Original", "Lightness", "Average", "Luminosity"]
    for idx, (img, title) in enumerate(zip(images, plt_titles)):
        axs[idx].imshow(img)
        axs[idx].set_title(title)
        axs[idx].set_xticks([])
        axs[idx].set_yticks([])
        
    plt.show()

if __name__ == "__main__":
    # # Setting a random seed to ensure repeatability - could be commented out during actual run
    # random.seed(42)
    image_path = "./leaves.jpg"
    plot_image(load_image(image_path))

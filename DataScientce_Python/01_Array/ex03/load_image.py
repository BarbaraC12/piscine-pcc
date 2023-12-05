from PIL import Image
import os
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Function that load and analyse an image
    print its format and its pixels content in RBG format [r, b, g]

    Parameters:
    path (str): the path to the image

    Returns:
    np.array: array of RGB colors
    """
    try:
        pre, ext = os.path.splitext(path)
        if ext.lower() not in (".jpg", ".jpeg"):
            raise TypeError(f"Format not supported: {ext}")
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found {path}")
        else:
            with Image.open(path) as img:
                w, h = img.size
                print(f"The shape of Image is: {h}, {w}, {img.layers}")
                pixels = np.array(
                    [img.getpixel((a, b)) for a in range(w) for b in range(h)])
            return pixels
    except Exception as err:
        print(Exception.__name__ + ":", err)
        return np.array([])


result = ft_load("landscape.jpg")
print((result))

from PIL import Image
import os


def ft_load(path: str) -> list:
    """
    Fonction that load and analyse an image
    print its format and its pixels content in RBG format [r, b, g]

    Parameters:
    path (str): the path to the image

    Returns:
    load (str)
    """
    try:
        if path.lower().endswith((".jpg", ".jpeg")):
            if os.path.exists(path):
                img = Image.open(path)
                w, h = img.size
                print(f"The shape of Image is: {h}, {w}, {img.layers}")
                pixels = []
                for a in range(w):
                    for b in range(h):
                        pixels.append(img.getpixel((a, b)))
                return [pixels]
            raise AssertionError("File not found:", path)
        raise AssertionError("Format supported: JPG and JPEG")
    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)
        return ""


print(ft_load("landscape.jpg"))

from load_image import ft_load
from PIL import Image
# go see here racoon on stack overflow
# https://stackoverflow.com/questions/37119071/scipy-rotate-and-zoom-an-image-without-changing-its-dimensions


def rotate(image: str):
    """
    """
    try:
        img = Image.open(image)
        w, h = img.size
        p_left = 200
        p_right = w
        p_top = h/2
        p_bottom = h
        depth = 1
        im1 = img.crop((p_left, p_top, p_right, p_bottom))  # A remanier ici
        im1.show()
        im1.close()
        img.close()
        return (img)
    except AssertionError as e:
        print(AssertionError.__name__ + ":", e)

    return


def main():
    """
    Take 2 list of int/float and return a list of BMI (IMC)
    Parameters:
    L1(list): a list of words separate by space
    L2(list): filter minimum lenght
    """
    try:
        print(ft_load("animal.jpeg"))
        return (rotate("animal.jpeg"))
    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)


if __name__ == "__main__":
    main()

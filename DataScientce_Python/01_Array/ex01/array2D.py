import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Print a shape of a list and return a truncated list from start to end

    Parameters:
    family (list): list of 2D array
    start (int): before this value trunc
    end (int): after this value trunc

    Returns:
    bmi (list): list of BMI (bmi = (weight / height^2))
    """
    try:
        if isinstance(family, list) and isinstance(start, int)\
         and isinstance(end, int):
            print(np.array(family).shape)  # print the shape of an np array
            print(np.array(family[start: end+1]).shape)  # from start to end
            return np.array(family[start: end+1]).tolist
        raise AssertionError(
            "Parameters must be in this order a list and two intergers")

    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)


fam = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(fam, 0, 2))
print(slice_me(fam, 1, -2))
print(slice_me(fam, 1, 78))
print(slice_me(fam, "1", -2))

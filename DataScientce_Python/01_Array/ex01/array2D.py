import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Print a shape of a list and return a truncated list from start to end

    Parameters:
    family (list): list of 2D array
    start (int): before this value trunc
    end (int): after this value trunc

    Returns:
    trunc (list): list truncated between star an end value
    """
    try:
        try:
            np_family = np.array(family)
        except ValueError:
            raise AssertionError(
                "Array dimension must have the same shape")
        valid_fam = np.all(np.isreal(np_family))
        valid_range = isinstance(start, int) and isinstance(end, int)
        if not valid_fam or not valid_range:
            raise TypeError(
                "Parameters must be a list of real and two integers")
        print(f"My shape are: {np_family.shape}")
        np_trunc = np_family[start: end]  # truncated np_list
        print(f"My new shape is: {np_trunc.shape}")
        return (np_trunc.tolist())

    except Exception as err:
        print(Exception.__name__ + ":", err)

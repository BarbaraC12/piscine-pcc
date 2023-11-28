import numpy as np


def give_bmi(
    h: list[int | float],
    w: list[int | float]
            ) -> list[int | float]:
    """
    Calculate of BMI based on two given list (BMI = IMC)

    Parameters:
    h (list): list of height in meter
    w (list): list of weight in kg

    Returns:
    bmi (list): list of BMI (bmi = (w / h^2))
    """
    try:
        np_h = np.array(h)
        np_w = np.array(w)
        if np_h.shape != np_w.shape:
            raise ValueError("list must have the same lenght")
        vali_h = np.all(np.greater_equal(np_h, np.zeros(np_h.shape))
                        & np.isreal(np_h))
        vali_w = np.all(np.greater_equal(np_w, np.zeros(np_w.shape))
                        & np.isreal(np_w))
        if not vali_h or not vali_w:
            raise TypeError("list must be positive int or float")
        np_bmi = (np_w / (np_h ** 2))
        return list(np_bmi)

    except Exception as err:
        print(Exception.__name__ + ":", err)


def apply_limit(
    bmi: list[int | float],
    limit: int
                ) -> list[bool]:
    """
    Try if BMI is above the limit

    Parameters:
    bmi (list): list of bmi
    limit (int): limit

    Returns:
    exceed (list): list boolean True if above the limit
    """
    np_bmi = np.array(bmi)
    try:
        va_bmi = np.all(np.greater_equal(np_bmi, np.zeros(np_bmi.shape))
                        & np.isreal(np_bmi))
        if not va_bmi:
            raise TypeError("list must be positive int or float")
        exceed = np_bmi <= limit
        return list(exceed)

    except Exception as err:
        print(Exception.__name__ + ":", err)

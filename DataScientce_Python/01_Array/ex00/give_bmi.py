from typing import List, Union


# def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
def give_bmi(height: List[Union[int, float]], weight: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Calcutator of BMI based on two given list (BMI = IMC)

    Parameters:
    height (list): list of height in meter
    weight (list): list of weight in kg

    Returns:
    bmi (list): list of BMI (bmi = (weight / height^2))
   """
    len_h = len(height)
    len_w = len(weight)
    bmi_list = []
    try:
        if len_h != len_w:
            raise ValueError("list must have the same lenght")
        for h, w in zip(height, weight):
            if not isinstance(h, (int, float))\
             or not isinstance(w, (int, float)):
                raise TypeError("list must be int or float")
            if h < 0 or w < 0:
                raise ValueError("value can't be negative")
            bmi = w / (h*h)
            bmi_list.append(bmi)
        return bmi_list

    except Exception as err:
        print(Exception.__name__ + ":", err)


# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]:
    """
    Try if BMI is above the limit

    Parameters:
    bmi (list): list of bmi
    limit (int): limit

    Returns:
    exceed (list): list boolean True if above the limite
   """
    exceed = []
    try:
        for n in bmi:
            if not isinstance(n, (int, float))\
             or not isinstance(limit, (int)):
                raise TypeError("list must be int or float")
            if n < 0 or limit < 0:
                raise ValueError("value can't be negative")
            exceed.append(n > limit)
        return exceed
    except Exception as err:
        print(Exception.__name__ + ":", err)

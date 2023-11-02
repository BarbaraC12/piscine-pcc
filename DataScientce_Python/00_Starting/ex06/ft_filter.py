def ft_filter(S: list, N: int) -> list:
    """Summary or Description of the Function

    Parameters:
    string  (str): list of words separate by space
    lenMin  (int): filter minimum lenght

    Returns:
    list: returning the list filtred

   """
    #  Comprehension list
    #  sum(1 for i in text if i.func()) == for i in text: if i.func(): val += 1
    filtred = []
    filtred = [word for word in S if len(word) > N]  # list comprehension
    return filtred

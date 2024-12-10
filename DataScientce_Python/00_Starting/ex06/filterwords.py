from sys import argv
from ft_filter import ft_filter


def main():
    """ Filterstring
    Take two parameters print the list without words.size() < N

    Parameters:
    S(str): a list of words separate by space
    N(int): filter minimum lenght

   """
    try:
        if len(argv) != 3 or not argv[2].isdigit() or argv[1].isnumeric():
            raise AssertionError("the arguments are bad")
        S = (lambda string: string.split())  # Lambda expression
        N = int(argv[2])
        print(ft_filter(S(argv[1]), N))
        return 0

    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)
        print("Usage:")
        print("\t$> python filterstring.py 'a string separate by space' 3")
        print("\t['string', 'separate', 'space']")


if __name__ == "__main__":
    main()

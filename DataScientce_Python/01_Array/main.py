from sys import argv


def main():
    """ fonction name
    Take 2 list of int/float and return a list of BMI (IMC)

    Parameters:
    L1(list): a list of words separate by space
    L2(list): filter minimum lenght

   """
    try:
        if len(argv) != 3 or not argv[2].isdigit() or argv[1].isnumeric():
            raise AssertionError("the arguments are bad")
        N = int(argv[2])
        return N

    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)
        print("Usage:")
        print("\t$> python filterstring.py 'a string separate by space' 3")
        print("\t['string', 'separate', 'space']")


if __name__ == "__main__":
    main()

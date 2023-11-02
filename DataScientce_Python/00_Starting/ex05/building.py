import sys
args = sys.argv


def building(text: str):
    """ Building
    This fonction take a single string and displays the sums of its:
     - Uppercase,
     - Lowercase,
     - Ponctuation
     - Space,
     - Digit
    """
    size = len(text)
    upper = sum(1 for i in text if i.isupper())
    lower = sum(1 for i in text if i.islower())
    space = sum(1 for i in text if i.isspace())
    digit = sum(1 for i in text if i.isdigit())
    ponct = sum(1 for i in text if i in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    #  Comprehension list
    #  sum(1 for i in text if i.func()) == for i in text: if i.func(): val += 1

    print(f"The text contains {size} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{ponct} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")
    return 0


def prompt() -> str:
    """ Prompt
    Call a prompt for take informations
    if catch EOF or interruption pass
    """
    text = ""
    try:
        text = input("What is the text to count?\n")
        text += "\n"
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass
    return text


def main():
    """ Analyzer
    If more than one argument is provided return an AssertionError
    Call a prompt if no argument is provided
   """
    la = len(args)
    try:
        if la > 2:
            raise AssertionError("more than one argument is provided")
        else:
            return building(args[1]) if la == 2 else building(prompt())
        
    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)


if __name__ == "__main__":
    main()

from sys import argv


def translate(lang: dict, text: str) -> str:
    """Translate text with given dictionary

    Parameters:
    lang (dict): the dictionary as reference
    text (str): string to translate

    Returns:
    str: The string translated

   """
    try:
        translated = [lang[char] for char in text.upper() if char in lang]
    except ValueError:
        raise AssertionError("plop")
    return ' '.join(translated)


def main():
    morse_dict = {
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', ' ': '/'
    }
    try:
        try:
            if len(argv) != 2:
                raise AssertionError("the arguments are bad")
            for letter in argv[1]:
                if not (letter.isalnum() or letter.isspace()):
                    raise AssertionError("the arguments are bad")
        except TypeError:
            raise AssertionError("plpp")
        print(translate(morse_dict, argv[1]))

    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)
        print("Usage:")
        print("\t$> python sos.py 'sos'")
        print("\t... --- ...")


if __name__ == "__main__":
    main()

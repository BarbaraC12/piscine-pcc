import sys

args = sys.argv


def odd_or_even(number: int):
    if number % 2:  # Si il y a un reste -> impaire
        return "I'm Odd."
    else:           # Sinon pair
        return "I'm Even."


try:
    try:
        if len(args) < 2:  # Si argv < 2
            exit()
        if len(args) > 2:  # Si argv > lève une exception
            raise AssertionError("more than one argument is provided")
        n = int(args[1])
    except ValueError:      # Si n n'est pas un digit lève une exception
        raise AssertionError("argument is not an integer")
    print(odd_or_even(n))   # Appel de odd_or_even()

# Capture les exceptions de type AssertionError
# et imprime le nom de l'exception avec le message associé
except AssertionError as err:
    print("AssertionError:", err)

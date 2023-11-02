def some_function(argument1):
    """Summary or Description of the Function

    Parameters:
    argument1 (int): Description of arg1

    Returns:
    int:Returning value

   """
    try:
        try:
            if argument1 is False:   #Si condition fausse
                raise AssertionError("Que c'est il passé?")
            n = int(argument1)    # cas ou args[1] n'est pas un digit = erreur
        except ValueError:      # Si une erreur survient
            raise AssertionError("Message d'erreur")
        return argument1

    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)
    

def main():
# your tests and your error handling
    return

if __name__ == "__main__":
    main()
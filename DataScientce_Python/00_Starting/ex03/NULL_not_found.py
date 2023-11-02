# Write a function that prints the object type of all types of "Null".
# Return 0 if it goes well and 1 in case of error.
# Your function needs to print all types of NULL.

def NULL_not_found(object: any) -> int:
    t = type(object)
    if object is None:
        print(f"Nothing: {object} {t}")
    elif object is False:
        print(f"Fake: {object} {t}")
    elif object == 0:
        print(f"Zero: {object} {t}")
    elif object == '':
        print(f"Empty: {t}")
    elif object != object:
        print(f"Cheese: {object} {t}")
    else:
        print("Type not found")
        return 1
    return 0

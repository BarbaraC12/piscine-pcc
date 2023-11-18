# Write a function that prints the object types and returns 42

def all_thing_is_obj(object: any) -> int:

    t = type(object)
    if t is list:
        print(f"List : {t}")
    elif t is tuple:
        print(f"Tuple : {t}")
    elif t is set:
        print(f"Set : {t}")
    elif t is dict:
        print(f"Dict : {t}")
    elif t is str:
        print(f"{object} is in the kitchen : {t}")
    else:
        print("Type not found")
    return 42

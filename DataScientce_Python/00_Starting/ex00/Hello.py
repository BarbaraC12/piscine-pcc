ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

new_list = "World!"
new_tuple = (ft_tuple[0], "France!")
new_set = "Paris!"
new_dict = "42Paris!"

# Les listes peuvent etre modifier grace a des fonctions propres aux listes
ft_list.pop()
ft_list.append("World!")
# Les tuple sont immuables ils ne peuvent pas etre modifier de l'interieur
ft_tuple = new_tuple
# Les valeurs des objets set sont immuable mais il est possible den add ou rm 
ft_set.discard("tutu!")
ft_set.add(new_set)
# ft_set = sorted(ft_set) # pour ordonned mais devient une liste
# Les dictionnaires sont bien plus permisifs ils fontionnent par clés/valeurs
ft_dict["Hello"] = new_dict


print(ft_list)  # ['Hello', 'World!']$
print(ft_tuple) # ('Hello', 'France!')$
print(ft_set)   # {'Hello', 'Paris!'}$
print(ft_dict)  # {'Hello': '42Paris!'}$
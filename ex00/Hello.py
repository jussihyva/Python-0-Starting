ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
# your code here
ft_list[1] = 'World!'
ft_tuple_list = list(ft_tuple)
ft_tuple_list[1] = 'Finland!'
ft_tuple = tuple(ft_tuple_list)
ft_set.remove("tutu!")
ft_set.add('Helsnki!')
ft_dict["Hello"] = 'Hive!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

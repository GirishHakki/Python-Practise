def convert_to_list_of_tuples(my_dict):
 return list(my_dict.items())

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list_of_tuples = convert_to_list_of_tuples(my_dict)
print("List of tuples:", my_list_of_tuples)
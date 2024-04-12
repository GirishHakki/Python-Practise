def convert_to_dict(lst):
 return dict(lst)

my_list_of_tuples = [("a", 1), ("b", 2), ("c", 3)]
my_dict = convert_to_dict(my_list_of_tuples)
print("Dictionary:", my_dict)
# Initializing dictionary
test_dict = {"Arushi": 22, "Giri": 24, "Priys": 23}

# Printing dictionary before removal
print("The dictionary before performing remove is : ", test_dict)

# Using del to remove a dict
# removes Mani
del test_dict['Giri']

# Printing dictionary after removal
print("The dictionary after remove is : ", test_dict)

# Using del to remove a dict
# raises exception
del test_dict['Giri']

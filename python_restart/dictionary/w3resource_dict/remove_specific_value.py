
original_dict = {
    'Theodore': {'user': 'Theodore', 'age': 45},
    'Roxanne': {'user': 'Roxanne', 'age': 15},
    'Mathew': {'user': 'Mathew', 'age': 21}
}

new_dict = {}

for key, value in original_dict.items():
    new_dict[key] = value["age"]

print(new_dict)

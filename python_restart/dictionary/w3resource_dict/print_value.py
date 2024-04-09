# Original list of dictionaries
list_of_dicts = [
    {'name': 'Theodore', 'age': 18},
    {'name': 'Mathew', 'age': 22},
    {'name': 'Roxanne', 'age': 20},
    {'name': 'David', 'age': 18}
]


specified_key = 'age'
list_of_values = []

 #list_of_values = [i[specified_key] for i in list_of_dicts]
 
for i in list_of_dicts:
     list_of_values.append(i[specified_key])
print(list_of_values)

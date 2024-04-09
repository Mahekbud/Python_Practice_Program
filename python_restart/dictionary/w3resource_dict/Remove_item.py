person = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178, 'weight': 50, 'height': 6}

delete_item = person.popitem()

print(person)

delete_item = person.pop("telephone")

print(person)

del person["weight"]

print(person)

person.clear()

print(person)

del person

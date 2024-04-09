# setdefault() method is used to set the value of a key with a default value if the key does not exist.

person_details = {"name": "Jessa", "country": "USA", "telephone": 1178}

x = person_details.setdefault("country", "Bronco")

print(x)
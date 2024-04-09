
my_dict = {'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}

#value_lengths = sum(len(value) for value in my_dict.values()

value_lengths = 0 

for value in my_dict.values():
    value_lengths += len(value)

print("Total length of all values:", value_lengths)



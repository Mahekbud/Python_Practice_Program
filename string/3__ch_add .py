a = "india"
b = "japan"

first = a[0] + b[0]

middle = a[int(len(a) / 2)] + b[int(len(b) / 2)]

last = a[len(a) - 1] + b[len(b) - 1]

result = first + middle + last

print(result)

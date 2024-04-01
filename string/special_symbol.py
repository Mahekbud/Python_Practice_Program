str1 = "PYnative29@#8496"

count = 0
sum = 0

for char in str1:
    if char.isdigit():
        count += 1
        sum += int(char)
        avg = sum/count
print (avg)
print(sum)

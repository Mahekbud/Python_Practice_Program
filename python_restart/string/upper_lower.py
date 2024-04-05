str = "MaHeK"

upper = []
lower = []

for i in str:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
        
result = ''.join(lower + upper)

print (result)
        
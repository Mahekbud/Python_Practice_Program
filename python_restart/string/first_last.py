s1 = "Abc"
s2 = "Xyz"

l = len(s1)

first = s1[0]+s2[l-1]

middle = s1[1]+s2[1]

last = s1[2]+s2[0]

result = first+middle+last 

print(result)

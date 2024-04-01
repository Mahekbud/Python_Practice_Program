str1 = "jenny"
str2 = "mahek"

result = str1[0]+str2[0]


middle = int(len(str1) / 2)

res = str1[:middle:] 

res = res + str2

res = res + str1[middle : ]

# res = str1[:3] + str2 + str1[-2 :]

print (res)
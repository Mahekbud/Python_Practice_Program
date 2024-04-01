# str1 = 'I am 25 years and 10 months old'



# for i in str1:
#     if i.isdigit():
#         print (i)

str1 = 'I am 25 years and 10 months old'
res = "".join([item for item in str1 if item.isdigit()])
print(res)
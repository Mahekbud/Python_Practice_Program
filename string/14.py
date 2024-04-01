str = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# string = []

# for i in str:
#     if i:
#         string.append(i)

string = list(filter(None, str))
        
print(string)

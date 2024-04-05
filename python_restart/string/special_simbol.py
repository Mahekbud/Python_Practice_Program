str1 = "P@#yn26at^&i5ve"

count = 0
digit = 0
symbol = 0

for char in str1:
    if char.isalpha():
        count += 1
    elif char.isdigit():
        digit += 1 
    else:
        symbol += 1
        
print("char : ",count ,"Digits :" , digit,"symbol : ",symbol)


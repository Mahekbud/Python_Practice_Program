



number = int(input("Enter number"))
Reverce = 0
temp = number
    
while(number != 0):
        n = number % 10
        Reverce = Reverce*10 + n
        number = number // 10
        
print("reverce number",Reverce)
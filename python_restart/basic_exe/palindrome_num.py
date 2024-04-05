def palindrome(number):
    print("Reverce Number",number)
    
    Reverce = 0
    temp = number
    
    while(number != 0):
        n = number % 10
        Reverce = Reverce*10 + n
        number = number // 10
        
    
    if temp == Reverce:
        print("palindrome number")
    else:
        print("Not palindrome Number")
        
palindrome (12321)
        
        

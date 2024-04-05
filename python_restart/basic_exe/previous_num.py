print("Currtent Number And previous Number")
previousNumber = 0

for i in range(1,11):
    Number = previousNumber + i
    
    print("current Number",i , "previous Number",previousNumber ,"sum : " , Number)
    
    
    previousNumber = i
    
    
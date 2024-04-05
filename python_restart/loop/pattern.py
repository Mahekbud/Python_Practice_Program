row = 5

for i  in range(0,row):
    for j in range(0,i+1):
        print("*",end = " ")
    print(" ")   
for i in range (0,row+1):
    for j in range(row+1,i,-1):
        print("*",end = " ")
    print(" ")
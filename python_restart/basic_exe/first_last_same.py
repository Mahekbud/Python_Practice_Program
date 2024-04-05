def First_last(List):
    print("Enter List",List)
    
    First = List[0]
    Last = List[-1]
    
    if First == Last :
        return True
    else:
        return False
    
List = [10,20,30,40,50,10]
print("result",First_last(List))




    
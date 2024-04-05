def result_num(list1,list2):
    empty_list = []
    
    for i in list1:
        if i % 2 != 0:
            empty_list.append(i)
            
            
            
    for j in list2:
        if j % 2 == 0 :
            empty_list.append(j)
    
    print(empty_list)
    
    
    
list1 = [10,20,25,30,67]
list2 = [65,40,35,48,56]


result_num(list1,list2)
def reverse(list):
    r_list=[]
    
    for i in range(0,len(list)):
        r_list.append(list[len(list)-i-1])
       
    return r_list   

def flatten(list):
  
  f_list=[]
  
  for i in list:
      if type(i) is list:
          f_list.extend(flatten(i))
      else
          f_list.append(i)
        
  return f_list      



a= input('')        
repeat = []                           
                      
for i in a:                          
    b= a.count(i, 0, len(a))   
    if b>1 and i not in repeat:         
        repeat.append(i) 
print(repeat)
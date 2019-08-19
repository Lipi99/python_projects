# python program to print a star pattern 
def pattern ( n ):   # n=3          
    list = []   # list = [] here u have taken list as the variable name
    # and there is also a bultin fucntion named list right? yes 
    # so, if u ever want to use that list() function, u won't be able to
    # because now list is a variable, not a function got it? okay done 
    for i in range ( 1 ,n+1 ):      
        list.append ("*" * i) 
        
    new_list = ("\n".join (list))   # new_list = "*\n**\n***" which is actually a string  
    return new_list  # return new_list

pattern_rows = int (input ("enter the number of maximum rows: " ))  # 3
y = pattern (pattern_rows)    # calles function with argument 3
print (y) # y = "*\n**\n***" , so correct


# output sahi hai, but method galat hai!! 0 marks
# kya???
# now see closely
# so method sahi hai actually, full marks!!
# but 0.5 deducted!! ok  
# next program
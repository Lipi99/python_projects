# python proram to swap first and last element in a list
def swap_list (new_list):            # passing list variable to new_list
    new_list [0], new_list [-1] = new_list [-1], new_list [0]  # new_list[0]= 1. [-1]=5 and swapping
    # with new_list[-1]=5 .new_list[0]=1 
     return new_list 
 
list = [1,2,3,4,5]   # list h ye

print(swap_list(list)) 


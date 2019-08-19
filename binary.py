
def everything_to_decimal(number, base):            
    sum = 0                                  
    p_v = 0
    for i in number[::-1]:                                           
        sum += int(i) * 2**p_v                      
        p_v += 1                                    
    print (sum)                                   

bi_num = str (input ("enter the number: "))            
num_system = int (input ("enter the base digit: "))      
 
everything_to_decimal (bi_num , num_system)


# h.w. -> make any 2 programs on your own ok
# ake sure you make the programs before we start tomorow. and use functions in them
# also, don't copy from google yes sure
# whatever program u make, just make sure u use functions to implement the logic of that program okay
# gd nt
# good night
# 🤣🤣🤣🤣 copying no i think this will work for number reversing
# thats why i said use while loop not for loop okkkk
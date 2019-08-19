# fibonacci program
"""
TASK: Make a program to get a number as input
and display the fibonacci series upto that number.
eg. 
Enter a number: 21
1, 1, 2, 3, 5, 8, 13, 21    # only this much if the input had been 21, we would include that in our
output as well. Like this. Got the program? 
"""

num = int (input("enter the number: "))
first_digit = 0
second_digit = 1
sum = first_digit + second_digit    
print ("fibonacci series is:")
 
result_List = []   

while sum <= num: 
    result_List.append(str(sum))    
    sum = first_digit + second_digit 
   ok
    first_digit =second_digit
    second_digit = sum

result_string = ', '.join(result_List)  
print("Result:",result_string)  

#

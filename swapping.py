# python program to swap the values of two variables
def swap (x,y):
    x,y = y,x     # nice
    # in python, swapping is done like this ok
    return (x,y)

num1 = int (input ("enter the value of 1st variable: "))
num2 = int (input ("enter the value of 2nd variable: "))  
print ("value before swapping: num1={0} and num2 = {1}  " . format (num1, num2)) # nice, string formatting... 
print("value after swapping, value after sapping: {0}".format(swap (num1, num2)))

 

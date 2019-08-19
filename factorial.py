# python program to find factorial of a number 
def fact (x):
    if x == 0 :
        return 1
    else :
        return x * fact ( x - 1 )

num = int (input("enter the numer: "))
print (fact (num)) 

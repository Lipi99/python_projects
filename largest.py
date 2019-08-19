# python program to find largest to three numbers
num1 = float(input("Enter first number: "))        # num1 = 2
num2 = float(input("Enter second number: "))       # num2 =3 
num3 = float(input("Enter third number: "))         # num3 = 4

def largest_num (a,b,c):                         # function definition and passing three variables a, b,c
    if (a>b) and (a>c):                          #  2 !> 3
        largest = a
    if (b>a) and (b>c):                           # 3 > 2 but 3 !> 4
        largest = b                               
    else : 
        largest = c                        # 4 >2 and 4>3
    return largest

result = largest_num (num1,num2,num3)
print (result)                                        # 4

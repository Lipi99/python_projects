
def palindrome (n):  
    reverse = 0
    new_number = n
    # n = 101
    while (n>0): # 101>0, so enters loop   |  10>0, so enters loop   | 1>0, enters loop | 0>0 is false, exit loop
        remainder = n % 10   # r=1 | r=0 | r =1 
        reverse = reverse *10 + remainder    # rev = 0*10 + 1=1  | rev = 1*10 + 0 = 10 | rev = 10*10 + 1 = 101
        n = n //10   # n  = 101//10 = 10 | n = 10//10 = 1 | n = 1//10 = 0
    if reverse == new_number:  # now, n was 0 when we had exited loop, so, rev==n is 101 == 0 is false
        return True
    else: # comes here
        return False # Flase is returned
 
num = int (input("enter the number: "))
print(palindrome (num))


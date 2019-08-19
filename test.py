# prime number programme
num = int (input ("enter a number: "))  
for i in range (2,(num//2)+1): 
    if ( int (num % i == 0) ):  
        print('not prime number')       
        prime = False
        break
if prime == True:
    print ("prime number")
    

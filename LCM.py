# make function check_prime(num) -> return True or False

# make a function get_factors(num) -> return a list of prime factors of that number

# make a function get_lcm(num1, num2) -> return lcm of these 2 numbers using get_factors function!

def prime (n):
    if n <= 1 :
        return False
    for i in range (2,n): 
        if n % i == 0: 
            return False  
    return True

def get_factors (n):
    prime_factors = [] 
    for i in range (2,n):
        if n % i == 0:
            if (prime (i)):
                prime_factors.append(i)
    return (prime_factors)            



def get_lcm (num1 , num2 ):
    num1_factors = get_factors (num1) 
    num2_factors = get_factors (num2)

    common_factors = []     

    result = 1  
    for n in common_factors :
        result = result * n
    return result


print (get_lcm (10, 15))




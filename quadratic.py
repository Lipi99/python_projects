def quadratic (a,b,c): # hmmm.. function definition, i'll skip it
    d = ((b*b) - (4 *a* c))**0.5  # comes here, processes this equation 
    x = (-b-d)/(2*a) # this too
    y = (-b + d)/(2*a) # this too.
    return [x,y]    # hm.. return, i must return this result as a list of [x,y]

a = (float(input("enter the number: ")))
b = (float(input("enter the number: ")))
c = (float (input("enter the number: ")))
roots_list = quadratic(a ,b , c) # now this result will get stored in the roots_list variable
print(roots_list)   
# come in LCM file!
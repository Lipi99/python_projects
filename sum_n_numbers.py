# python program to find sum of n numbers 
n = int (input ("enter a nnumber"))     # with n = 5           
sum = 0
total = 0
for i in range (n+1):
    sum = sum + n  

print (sum)
# this for loop gives output 30 right? ye 

# while loop to give the same output
# first make an index variable
i=0
while (i<n+1): # sry, n+1 hoga, because for loop mai bhi n+1 kiya tha
    total+=n
    i+=1

print(total)

# ok, 
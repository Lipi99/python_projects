# python program to place Even and Odd elements of a list in Two Different lists
my_list = []
max_value = int (input("enter the number of elements of list:\t"))

for i in range (1, 1 + max_value ):
        all_elements = int(input("enter the elements: "))
        my_list .append( all_elements )

even_list = []
odd_list = []
for j in my_list :
        if ( j % 2 == 0):
                even_list .append ( j )
        else:
                odd_list .append ( j )

print ("enter even number list\t", even_list)
print ("enter odd number list\t", odd_list)
        

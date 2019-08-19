# python program to perform linear search

my_list = []
num = int (input ("enter the maximum size of the list: ")) # to get maximum size of list
 
for n in range (num):
    numbers = int (input ("enter the numbers: "))    # to input all the numbers of list one by one
    my_list.append ( numbers )  # appending all the numbers to the list

found = False

search_num = int (input ( "enter the element to be searched: "))
for i in range (len (my_list)):
    if search_num == my_list [i]:
        found = True
        print ("found at position =", i+1)
        break

if (not found) :
    print ("not found")

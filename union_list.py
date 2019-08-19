# python program to find union of two lists
# union is unique elements of two elements which different for concatination
my_list1 = []
num = int (input ( "enter the maximum number of elemnts in first list:\t" ))

for i in range (num):
    numbers1 = int (input ("enter the elements of list 1: "))
    my_list1.append (numbers1)

my_list2 = []
num2 = int (input ( "enter the maximum number of elemnts in second list:\t" ))

for i in range (num2):
    numbers2 = int (input ("enter the elements of list 2: "))
    my_list2.append (numbers2)

union_of_two_lists = list (set (). union (my_list1 , my_list2 ))
print (union_of_two_lists)

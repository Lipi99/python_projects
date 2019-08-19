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
        
# hi 
# hi
# ab zara try kar, iss progra ko save kar, gitub desktop khol aur
# commit kar ke dekh
# ha uss prr khol diya..phir?? 
#uss par kis par? github destop 
# ha, now clik on your repo, and see if it shows u the option to commit to mster at 
# the bottom left
# src dekh joi maine kal bheji thi
# summary m kya doo ?? yaha ?? 
# # aur description m ??
# kuch bhi dede kuch bhi dede kuch bhi
# nhi ho rha yaar uss prr click 
# ek baar discord prr aana please, nahi aise hi save kar
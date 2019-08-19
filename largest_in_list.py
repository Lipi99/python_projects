# python program to find largest element in a list
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])  # instead of a[n-1] u could have written a[-1]


# come to the next program
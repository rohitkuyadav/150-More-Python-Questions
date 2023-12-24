# Python Program to print the fabonaci series
# the number which is the sum of previous two
n = int(input("Enter the limit: "))
a,b = 0,1

for i in range(n):
    print(a,end= " ")
    c = a+b
    a =  b
    b = c

# 0 1 1 2 3 5 8 13 21 34 
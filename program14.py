# Python program to check if the number is prime or not

num =  int(input("Enter the number: "))

if num>1:
    for i in range(2,int(num/2)+1):
        if num%i==0:
            print(f"{num} is not a prime number")
            break

    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
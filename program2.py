# Python program to do Aruthematic Operation Addition and Substractions

num1 = float(input("Enter the number 1: "))
num2 = float(input("Enter the number : "))

print(f"""

1. Addition
2. Division
      """)
option = int(input("ENter option(1/2): "))

if option ==1:
    print("Addition of Two number is: {}".format(num1+num2))

elif option ==2:
    print("Division of Two number is: {}".format(num1/num2))
    
else:
    print("Please select the one ")


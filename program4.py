# Python Program to swap two Variable

"""
Algo Used: 
num1 = 10
num2 = 20
num1 = num2 (now num1 = 20) and num2 = num1>>now if you print(num1,num2) then the ouput became 20 20.. this is because
num2 return the value of num1 that is same value

so to resolve this Problem use of temporary variable
code below
"""

num1 = 10
num2 = 20

temp = num2
num2 = num1
num1 = temp

print(f"""
Before Swapping: num1 = 10 
                 num2 = 20
      
After Swapping : num1 = {num1}
                 num2 = {num2}
""")
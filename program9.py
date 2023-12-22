# Python Program to Solve Quadratic Equations

import math

print("""
ax^2+bx+c
""")

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

D = b**2-4*a*c

if D>0:
    # Roots are reals and Distinct
    root1 = (-b + math.sqrt(D))/2*a
    root2 = (-b - math.sqrt(D))/2*a
    print("Root1: {}".format(root1))
    print("Root2: {}".format(root2))

elif D ==0:
    # REAL and Repleated root
    root = -b/2*a
    print("Root: {}".format(root))

else:
    #complex Roots
    real = -b/2*a
    imaginary = math.sqrt(abs(D))/2*a
    print(f"Root1: {real}-{imaginary}i")
    print(f"Root1: {real}+{imaginary}i")

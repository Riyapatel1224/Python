import sys
from tkinter import Y
from unittest import result

try:
    x=int(input("x: "))
    y=int(input("y: "))

except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try:
    result=x/y 
except ZeroDivisionError:
    print("Error: Cannot divided by 0.")
    sys.exit(1)

print(f"{x}/{y}={result}")
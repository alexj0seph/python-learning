#prompts the user to input their name, stores it in the variable "name" and then prints a greeting message 
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")
'''
    Enter your name: GeeksforGeeks
    Hello, GeeksforGeeks ! Welcome!
'''

#This program asks the user for a value, stores it as a string and then prints it back.
val = input("Enter your value: ")

print(val)
'''
Output

    Enter your value: 123
    123
'''
#This program checks the data type of user input to confirm that both number and name are stored as strings.
num = input("Enter number:")
print(num)
name1 = input("Enter name: ")
print(name1)
# Printing type of input value
print ("type of number", type(num))
print ("type of name", type(name1))
"""
Output

    Enter number: 45
    45
    Enter name: John
    John
    Type of number: <class 'str'>
    Type of name: <class 'str'>
"""

#Converting Input into Numbers

#This program converts user input into an integer.

num = int(input("Enter a number: "))

print(num, "is of type", type(num))
'''
Output

    Enter a number: 25
    25 is of type <class 'int'>
'''

#Floating-Point Input

#This program converts user input into a float (decimal number).

floatNum = float(input("Enter a decimal number: "))
print(floatNum, "is of type", type(floatNum))
'''
Output

    Enter a decimal number: 19.75
    19.75 is of type <class 'float'>
'''

#Taking Multiple Inputs

#This program takes two numbers from the user in one input line, splits them and prints them separately.
x, y = input("Enter two numbers separated by space: ").split()
print("First number:", x)
print("Second number:", y)
'''
Output

    Enter two numbers separated by space: 10 20
    First number: 10
    Second number: 20
'''

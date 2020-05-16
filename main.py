X = 0
y = 0
ar_op=""

print("Welcome to Python Calculator! You can use basic arithmetic operations:\naddition (+),\nsubtraction (-),\nmultiplication (*),\ndivision (/)")
ar_op = input("Please enter the artimetic operation that you want to use:").lower()

if ar_op == "+" or ar_op == "addition":
    x = int(input("Please enter the first number x= "))
    y = int(input("Please enter the second number y= "))
    print("Result is: "+str(x+y))
elif ar_op == "-" or ar_op == "subtraction":
    x = int(input("Please enter the first number x= "))
    y = int(input("Please enter the second number y= "))
    print("Result is: "+str(x-y))
elif ar_op == "*" or ar_op == "multiplication":
    x = int(input("Please enter the first number x= "))
    y = int(input("Please enter the second number y= "))
    print("Result is: "+str(x*y))
elif ar_op == "/" or ar_op == "division":
    x = int(input("Please enter the first number x= "))
    y = int(input("Please enter the second number y= "))
    print("Result is: "+str(x/y))
else:
    print("Calculator doesn't recognize this operation.")
# The try block lets you test a block of code for errors.
try:
    x = int(input("What's x? "))
    
# The except block lets you handle the error.
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
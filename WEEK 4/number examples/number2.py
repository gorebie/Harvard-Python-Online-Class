while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
    # it allows you to exit a loop when an external condition is met.
    
print(f"x is {x}")
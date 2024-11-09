def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x?"))
        except ValueError:
            pass 
        # pass: print("x is not an integer")

main()
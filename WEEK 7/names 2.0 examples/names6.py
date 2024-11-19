names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rsplit())

for name in sorted(names):
    # if you wanna reverse it (Z to A)
    # for name in sorted(names, reverse=True):
    print(f"hello, {name}")
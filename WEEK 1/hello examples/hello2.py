# ask user for their name
name = input("What's your name? ").strip().title()

# split user's name into first name and last name
first, last = name.split(" ")

# Remove whitesapce from str
name = name.strip()

# Capitalize user's name
name = name.title()

# say hello to user
print(f"hello, {first}")
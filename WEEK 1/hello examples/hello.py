# ask user for their name
name = input("What's your name? ").strip().title()

# remove whitespace from string aka str
name = name.strip()

# capitalize user's name
name = name.capitalize()

# capitalize user's full name
name = name.title()

name = name.strip().title()

# say hello to user
print("hello,", name)

# end cmd writes next to it instead of another/next line
print("hello, ", end="")
print(name)

print("hello, ", name, sep="Miss ")

# you can use ' and " on python
print("hello, \"friend\"")

# format string
print(f"hello, {name}")



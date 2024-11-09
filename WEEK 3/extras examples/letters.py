def main():
    print(write_letter("Mario", "Princess Peach"))
    print(write_letter("Luigi", "Princess Peach"))
    print(write_letter("Daisy", "Princess Peach"))
    print(write_letter("Yoshi", "Princess Peach"))

def write_letter (recivever, sender):
    return f"""
    Dear {recivever}

    You are cordially invited to a ball at 
    Peach's Castle this evening, 7:00PM.

    Sincerely,
    {sender}
"""

main()
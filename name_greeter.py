# Ask the user for their full name
user_input = input("Please enter your full name: ")

# Split the string into a list of names based on spaces
name_parts = user_input.split()

# Check if the user entered two or more names
if len(name_parts) >= 2:
    # Greet them using only the first item in the list
    first_name = name_parts[0]
    print(f"Hello, {first_name}! Great to meet you.")
else:
    # Friendly message if they only typed one word
    print("Oops! It looks like you only entered one name. Next time, please provide your full name.")
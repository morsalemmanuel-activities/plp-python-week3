# BUG: The original line was missing a closing quotation mark, causing a SyntaxError. Fixed by adding a " at the end of the text.
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: The original line tried to print literal text "nmae" instead of referencing the variable. Fixed by using an f-string and fixing the typo to {name}.
print(f"Nice to meet you, {name}")

age = input("How old are you? ")

# BUG: The original line threw a TypeError because 'age' is a string and cannot be mathematically added to the integer 1. Fixed by converting 'age' to an int, calculating the sum, and using an f-string.
next_year_age = int(age) + 1
print(f"Next year you will be {next_year_age}")
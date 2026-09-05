# Ask for age and immediately convert the string input into an integer
age = int(input("Please enter your age: "))

# Create and store the Boolean variable
is_adult = age >= 18

# Print the Boolean value explicitly as requested
print(f"Is adult status: {is_adult}")

# Define your ticket prices
adult_price = "Ksh 500"
child_price = "Ksh 200"

# Use if / else logic to determine the final price based on the Boolean
if is_adult:
    print(f"Ticket Price: Full adult price applies. That will be {adult_price}.")
else:
    print(f"Ticket Price: Child discount applies! That will be {child_price}.")
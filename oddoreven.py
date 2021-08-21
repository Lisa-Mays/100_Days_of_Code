# Display Welcome
print("Welcome to the Odd or Even Determination Machine")

# Prompt for a number
number = int(input("Which number do you want to check? "))

# Check if the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
  print("This is an even number.")

# Otherwise if the number cannot be divided by 2 with 0 remainder
else:
  print("This is an odd number.")


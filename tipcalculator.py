# Display welcome message
print("Welcome to the tip calculator.")

# Prompt for the total cost of the bill and set as float
original_bill = float(input("What was the total bill? $"))

# Prompt for the tip percentage 10, 12 or 15 percent and convert to int
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Prompt for how many people are splitting the bill and set to int
total_diners = int(input("How many people to split the bill? "))

# Calculate the tip and set as float
tip_percentage = tip * .01
float(tip_amount) = original_bill * tip_percentage

# Calculate the bill plus the tip
total_bill = original_bill + tip_amount

# Calculate the total bill divided by the number of people
split_bill = round(total_bill / total_diners, 2)

# Display the amount each person should pay rounded to decimal places
split_amount = print(f"Each person should pay: ${split_bill}")
print(split_amount)

# Prompt for current age in years
current_age = input("What is your current age in years?\n")

# Convert str to int
current_age = int(current_age)

# Assume life length is 90 years
max_life_years = 90

# Calculate how many years are left given the age input
years_left = max_life_years - current_age

# Calculate and round how many days, week, and months are left
days_left = round(years_left * 365)
weeks_left = round(years_left * 52)
months_left = round(years_left * 12)

# Display how many days, weeks, and months are left
final_result = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(final_result)

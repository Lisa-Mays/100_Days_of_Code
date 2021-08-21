# Display welcome
print("This program will determine if a given year is a leap year.")

# Prompt for a year
given_year = int(input("Please enter a year: "))
leapyear = True

# Math time
if given_year % 4 == 0:
  if given_year % 100 == 0:
    if given_year % 400 == 0:
      print(f"{given_year} is a Leap year.")
    else:
      print(f"{given_year} is NOT a Leap year.")
  else:
    print(f"{given_year} is a Leap year.")
else:
  print(f"{given_year} is NOT a Leap year.")

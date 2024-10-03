# Jada Sinclair
# 10/3/2024
# P2LAB2
# Using dictionary with user input

# Create the dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silerado":26}

# Get the keys only
keys = cars.keys()
print(keys)

# Prompt the user to give one of the keys (car)
user_choice = input("Enter a vehicle to see it's mpg: ")
print()

# Show the user mpg for their selected car
print(f"The {user_choice} gets {cars[user_choice]} mpg.")

# Get the amount of miles to be driven
miles_to_drive = float(input(f"How many miles will you drive the {user_choice}"))

# Calculate gallons needed to drive distance
gallons_needed = miles_to_drive/cars[user_choice]

# Display gallons needed to the user
print(f"{gallons_needed:.2f} gallons of gas are needed to drive the {user_choice} {miles_to_drive} miles.")

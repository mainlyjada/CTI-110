# Jada Sinclair
# 9/26/24
# P1HW2
# Creating a program that does basic math  


print ("This program calculates and displays travel expenses")
print ()

# Get user to enter thier budget (Enter as an integer)
budget = float(input("Please enter your budget: "))

# Get users travel destination
destination = input("Please enter your travel destination: ")

# Get users amount they will spend on gas
gas = float(input("Please enter how much you think youll spend on gas: "))

# Get users amount they will spend for accommodation
amount = float(input("Please enter how much youll spend on accommodation/hotel: "))

# Get user to enter how much they will spend on food
food_budget = float(input("Last, enter how much you will spend on food: "))

# Display the location and budget

print ("destination" ,  destination)
print ("budget" , budget)

print ()

# Display gas, food and accommodation

print("gas" , gas)
print("accommodation" , amount)
print("food" , food_budget)

print ()
print("--------Travel Expenses--------")

print(f"{'Destination:':<30}{destination}")
print(f"{'Budget:':<30}${budget:,.2f}")
print(f"{'Gas:':<30}${gas:,.2f}")
print(f"{'Accommdation:':<30}${amount:,.2f}")
print(f"{'Food:':<30}${food_budget:,.2f}")

print("-------------------------------------")
total = gas+ amount + food_budget
total2 = budget - total

print ()
print (f"{'remaining balance:':<30}${total2:,.2f}")

























# Jada Sinclair
# 10/10/2024
# P2HW2
# Program should store grades in a list

# Allow user to give list items
num1 = float(input("Enter a grade for module 1: "))
num2 = float(input("Enter a grade for module 2: "))
num3 = float(input("Enter a grade for module 3: "))
num4 = float(input("Enter a grade for module 4: "))
num5 = float(input("Enter a garde for module 5: "))
num6 = float(input("Enter a grade for module 6: "))

'''
# Empty list
num_list = []

# Add variables to the list
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)
'''
 # Create the list with the variables
num_list = [num1, num2, num3, num4]
print("-------------Results------------")

#num_list.append(100)

# Print list
print(num_list)

# Find the average
average = sum(num_list)/len(num_list)


# Using functions with list
print(f"Lowest grade  {min(num_list)} !!")
print(f"Highest grade {max(num_list)} !!")
print(f"Sum of grades {sum(num_list)} !!")
print(f"Average {average }!!")


print("-----------------------------------")

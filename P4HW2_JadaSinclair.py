# Jada Sinclair
# 11/7/2024
# P4HW2
# 

# finalize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Loop to get employee data
while True:
    # Get employee name
    name = input("Enter employee's name or 'Done' to stop: ")
    
    # get value to terminate the loop
    if name.lower() == "done":
        break
    
    # Get pay rate and hours worked
    try:
        pay_rate = float(input("Enter pay rate: $"))
        hours_worked = float(input("Enter hours worked: "))
    except ValueError:
        print("Invalid input! Please enter numeric values for pay rate and hours worked.")
        continue

    # Calculate regular and overtime pay
    if hours_worked > 40:
        regular_pay = 40 * pay_rate
        overtime_pay = (hours_worked - 40) * (pay_rate * 1.5)  # Overtime is paid at 1.5x rate
    else:
        regular_pay = hours_worked * pay_rate
        overtime_pay = 0
    
    # Calculate gross pay (regular pay + overtime pay)
    gross_pay = regular_pay + overtime_pay
    
    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1
    
    # Display results for this employee in one line
    print()
    print(f"{name}")
    print(f"Regular Pay ${regular_pay:.2f}  Overtime Pay ${overtime_pay:.2f}  Gross Pay ${gross_pay:.2f}")

# Display final totals after all employees are entered
print("\n--- Final Results ---")
print(f"Number of Employees Entered: {num_employees}")
print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
print(f"Total Regular Pay: ${total_regular_pay:.2f}")
print(f"Total Gross Pay: ${total_gross_pay:.2f}")




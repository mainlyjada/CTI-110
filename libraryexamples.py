# In- class examples of using built-in libraries

# Import datetime libraries so we can use it in the program
import datetime

import  random

# Get the current date and time
curr_time = datetime.datetime.now ()

# Display date/time
print (f"The current date/time is {curr_time}")

# Generate random numbers
random_1 = random.randint (1, 10)
random_2 = random.randint (50, 100)

# Dsiplay the random values
print (f"{random_1} times {random_2} equals {random_1 * random_2}")



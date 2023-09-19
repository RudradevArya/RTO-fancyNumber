'''#  A function to find all the 4 digit numbers whose sum of digits is equal to a given value
def find_numbers(value):
  # Initialize an empty list to store the numbers
  numbers = []
  # Loop through all the 4 digit numbers
  for i in range(0000, 10000):
    # Check if the sum of digits is equal to the value
    if sum_of_digits(i, value):
      # Add the number to the list
      numbers.append(i)
  # Return the list of numbers
  return numbers

# Print all the 4 digit numbers whose sum of digits is 6
print(find_numbers(6))


'''

# A function to find the digital root of a number
def digital_root(n):
  # If n is zero, return zero
  if n == 0:
    return 0
  # Otherwise, use the formula
  else:
    return 1 + ((n - 1) % 9)

# A function to find all the numbers whose digital root is equal to a given value
def find_numbers(value):
  # Initialize an empty list to store the numbers
  numbers = []
  # Loop through all the possible numbers
  for i in range(0, 10000):
    # Check if the digital root is equal to the value
    if digital_root(i) == value:
      # Add the number to the list
      numbers.append(i)
  # Return the list of numbers
  return numbers

# Print all the numbers whose digital root is 6
print(find_numbers(6))

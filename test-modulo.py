"""Uses of Modulo"""

# Given a number, % and // can be used to get each digit. For a 3-digit number user_val like 927:
user_val = 927

ones_digit = user_val % 10
tmp_val = user_val // 10

tens_digit = tmp_val % 10
tmp_val = tmp_val // 10

hundreds_digit = tmp_val % 10

print(f'The number {user_val} has {ones_digit} in the ones place, {tens_digit} in the tens place,', end='')
print(f'and {hundreds_digit} in the hundreds place.')

# Check if number is Even or Odd. However, checking the least significant bit is better.
# Using user_val from above.

isEven = user_val % 2 == 0
print(isEven)
isOdd = user_val % 2 != 0 # Use != 0 vs == 1 because modulo in python with negative second operand will return -1
print(isOdd)

# Convert Units
my_inches = 79
inches = my_inches % 12 # gets the inches that cannot be evenly divided into feet
feet = my_inches // 12 # get the inches that can be divided into feet
print(f"{my_inches} inches = {feet} feet and {inches} inches.")

my_minutes = 3456
total_minutes = my_minutes % 60 # minutes not divisible into hours
hours = my_minutes // 60
total_hours = hours % 24   # Hours not divisible into days
total_days = hours // 24 # days are equal to the hours that are evenly divisible into days
print(f"{my_minutes} minutes = {total_days} days, {total_hours} hours and {total_minutes} minutes.")

# Check if number is a Prime number. Prime numbers contain only two factors, 1 and itself.
# Cipher.
# More to come.
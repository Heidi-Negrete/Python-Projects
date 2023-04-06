"""import time

print('I am dumb.', end=' ')
name = input('What is your name? ')
print('Ok, your name is', name)
time.sleep(2)
print('Once again I am asking...')
time.sleep(1)
name = input('What is your name? ')
print(f'Ok so your name is {name}')"""

# Given a number, % and // can be used to get each digit. For a 3-digit number user_val like 927:
user_val = 927

ones_digit = user_val % 10
tmp_val = user_val // 10

tens_digit = tmp_val % 10
tmp_val = tmp_val // 10

hundreds_digit = tmp_val % 10

print(f'The number {user_val} has {ones_digit} in the ones place, {tens_digit} in the tens place,', end='')
print(f'and {hundreds_digit} in the hundreds place.')


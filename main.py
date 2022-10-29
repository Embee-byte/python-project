print('This program is designed to solve combination of two numbers')
first_number = int(input("please input your fist number"))
second_number = int(input("please input your second number"))
factorial_n = first_number - 1
factorial_r =  second_number - 1
remainder = first_number - second_number
factorial_remainder = remainder - 1

while factorial_n > 0:
    first_number = first_number * factorial_n
    factorial_n = factorial_n - 1


while factorial_r > 0:
    second_number = second_number * factorial_r
    factorial_r = factorial_r - 1

while factorial_remainder > 0:
    remainder = remainder * factorial_remainder
    factorial_remainder = factorial_remainder - 1

denominator = remainder * second_number
result = first_number/denominator
print(result)
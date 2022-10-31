import sys

divisor_number = int(input())
bound_number = int(input())
max_number = -sys.maxsize

for number in range(0, bound_number+1):
    if 0 < number <= bound_number:
        if number % divisor_number == 0:
            max_number = number

print(max_number)

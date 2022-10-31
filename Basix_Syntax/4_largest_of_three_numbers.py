first_number = int(input())
second_number = int(input())
third_number = int(input())

if third_number < first_number > second_number:
    print(first_number)
elif third_number < second_number > first_number:
    print(second_number)
else:
    print(third_number)
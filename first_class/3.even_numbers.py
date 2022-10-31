n_numbers = int(input())

for i in range(0, n_numbers):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break

if number % 2 == 0:
    print("All numbers are even.")
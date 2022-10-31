number = float(input())

while True:
    if 1 <= number <= 100:
        break
    number = float(input())

print(f"The number {number} is between 1 and 100")
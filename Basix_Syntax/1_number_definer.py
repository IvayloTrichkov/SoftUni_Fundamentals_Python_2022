num = float(input())

if num == 0:
    print("zero")
elif 0 < num < 1:
    print("small positive")
elif num > 1000000:
    print("large positive")
elif num > 0:
    print("positive")

if num < 0:
    if 1 > abs(num) > 0:
        print("small negative")
    elif abs(num) > 1000000:
        print("large negative")
    else:
        print('negative')
number_of_orders = int(input())
total = 0

for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed <= 2000:
        the_price_for_the_coffee_is = price_per_capsule * days * capsules_needed
        print(f"The price for the coffee is: ${the_price_for_the_coffee_is:.2f}")
        total += the_price_for_the_coffee_is
    else:
        continue
print(f"Total: ${total:.2f}")
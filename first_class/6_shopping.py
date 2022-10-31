budget = int(input())

while True:
    product_price = input()
    if product_price != "End":
        product_price = int(product_price)
        budget -= product_price
        if budget < 0:
            break
    elif product_price == "End":
        break

if budget < 0:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")




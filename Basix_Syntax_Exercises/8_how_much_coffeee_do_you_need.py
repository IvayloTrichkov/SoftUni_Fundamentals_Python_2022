number_of_coffee_needed = 0
activity = ""
while activity != "END":
    activity = input()
    if activity == "coding" or activity == "dog" or activity == "cat" or activity == "movie":
        number_of_coffee_needed += 1
    elif activity == "CODING" or activity == "DOG" or activity == "CAT" or activity == "MOVIE":
        number_of_coffee_needed += 2
    else:
        continue

if number_of_coffee_needed > 5:
    print("You need extra sleep")
else:
    print(number_of_coffee_needed)





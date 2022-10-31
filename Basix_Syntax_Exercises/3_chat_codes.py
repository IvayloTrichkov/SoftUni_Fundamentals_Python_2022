n_numbers = int(input())
counter = 0

while True:
    counter += 1
    number_code = int(input())
    if number_code == 88:
        print("Hello")
    elif number_code == 86:
        print("How are you?")
    elif number_code < 88 and number_code != 86:
        print("GREAT!")
    else:
        print("Bye.")
    if counter == n_numbers:
        break

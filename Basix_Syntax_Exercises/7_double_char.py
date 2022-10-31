result = ""
while True:
    current_string = input()
    if current_string == "End":
        break
    if current_string == "SoftUni":
        continue
    for letters in current_string:
        result += letters*2
    print(result)
    result = ""

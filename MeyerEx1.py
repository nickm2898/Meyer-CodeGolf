def multiply(lists):
    result = 1
    for values in lists:
        result = result * values
    return result


a = int
while a is int:
    try:
        a = int(input("Enter first number: "))
    except ValueError:
        print("Not a number")

b = int
while b is int:
    try:
        b = int(input("Enter second number: "))
        while b < a:
            print("Error: second number must be a higher value than first number")
            b = int(input("Enter second number: "))
    except ValueError:
        print("Not a number")

include_b = (input("Is second number inclusive y/n? "))

if (include_b == "y") or (include_b == "n"):
    invalid_input = True
else:
    invalid_input = False

while invalid_input is False:
    if (include_b == "y") or (include_b == "n"):
        break
    else:
        invalid_input = False
    print("Invalid Input")
    include_b = (input("Is second number inclusive y/n? "))

if include_b == "y":
    b += 1

buh = []

for num in range(a, b):
    buh.append(num)

print(multiply(buh))

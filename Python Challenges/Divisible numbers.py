numerator = int(input("Enter the numerator : "))
denominator = int(input("Enter the denominator : "))

if denominator == 0:
    print("Denomiator can't be 0")
else:
    if numerator % denominator == 0:
        print("Both the numbers are divisible")
    else:
        print("Both the numbers aren't divisible")
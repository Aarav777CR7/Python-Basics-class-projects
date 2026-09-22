temperature = int(input("Enter today's temperature in Celsius: "))

if temperature < 20:
    outfit = "jacket"
    print("Wear a", outfit)
else:
    outfit = "t-shirt"
    print("Wear a", outfit)

    print("=" * 40)

    rain = input("Is it raining today? (yes/no): ")

    if rain == "yes":
        print("Bring an umbrella!")
    elif rain == "no":
        print("Enjoy your day")
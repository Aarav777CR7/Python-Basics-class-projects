grade = int(input("Enter the grade between 1 and 10 : "))

if grade >=1 and grade <= 3:
    print("Basic Level of coding")
elif grade >=4 and grade <= 5:
    print("Intermediate Level of coding")
elif grade >=6 and grade <= 8:
    print("Advance Level of coding")
elif grade >=9 and grade <= 10:
    print("Expertise Level of coding")
else:
    print("Invalid input")
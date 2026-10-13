print("Enter your marks obtained in 4 subjects: ")
English = int(input("English:"))
Maths = int(input("Maths:"))
Science = int(input("Science:"))
Sst = int(input("Sst:"))

total_marks = English + Maths + Science + Sst
average = int(total_marks / 4)

if average in range(81,100 ):
    print("Grade A")
elif average in range(61,80 ):
    print("Grade B")
elif average in range(41,60 ):
    print("Grade C")
else:
    print("Grade F")
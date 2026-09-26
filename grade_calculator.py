grade = int(input("Enter your grade:"))
if grade < 0 or grade > 100:
    print("Invalid marks.")

elif grade >= 90:
    print("Grade: A")

elif grade >= 80:
    print("Grade: B")

elif grade >= 70:
    print("Grade: C")

elif grade >= 60:
    print("Grade: D")

elif grade >= 40:
    print("Grade: E")

else:
    print("Grade: F")
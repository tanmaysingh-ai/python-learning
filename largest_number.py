a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a > b or a > c:
    print("First number is the largest number")
elif b > a or b > c:
    print("Second number is the largest number")
else:
    print("Third number is the largest number ")
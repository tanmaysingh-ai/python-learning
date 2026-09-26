correct_username = "tanmay"
correct_password = "12345"
username = input("Enter your username:")
password = (input("Enter your password:"))

if correct_username == username and correct_password == password:
    print("Login successful")
else:
    print("invalid username or password")

valid_password = "test123"
login_successful = False
for i in range (3):
    password = input("Enter password: ")
    if password == valid_password:
        print("Login successful")
        login_successful = True
        break
    else:
        print("Incorrect password")
if not login_successful:
    print("Account locked")


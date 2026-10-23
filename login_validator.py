valid_username = "admin"
valid_password = "test123"
username = input("Username: ")
password = input("Password: ")
if username == valid_username and password == valid_password:
    print("Login successfull")
else:
    print ("Invalid username or password")
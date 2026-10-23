def login(username, password):
    if username == "admin" and password == "test123":
        return ("Login successful")
    else: 
        return ("Login failed")

result = login("admin", "test123")
print(result)

result = login("admin", "wrong")
print(result)
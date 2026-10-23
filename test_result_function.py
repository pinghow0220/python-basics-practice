users = [
    {"username": "admin",
     "password": "admin123",
     "expected_result": "Login Successful"
     },
    {"username": "tester",
     "password": "tester123",
     "expected_result": "Login failed"
     },
    {"username": "invalid",
     "password": "wrong",
     "expected_result": "Login failed"
     }
]


def login(username, password):
    if username == "admin" and password == "admin123":
        actual = "Login Successful"
    else:
        actual = "Login failed"
    return actual
def check_result(expected, actual):
    if expected == actual:
        return ("Pass")
    else:
        return ("Fail")

for user in users:
    login_result = login(user["username"], user["password"])
    result = check_result (user["expected_result"], login_result)
    print("Actual:", login_result)
    print("Result:", result)

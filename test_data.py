users = [
    {"username": "admin",
     "password": "admin123",
     "expected_result": "Login Successful"
     },
    {"username": "tester",
     "password": "tester123",
     "expected_result": "Login Successful"
     },
    {"username": "invalid",
     "password": "wrong",
     "expected_result": "Login failed"
     }
]

for user in users:
    print ("Testing user: " + user["username"])
    print ("Expected: " + user["expected_result"])
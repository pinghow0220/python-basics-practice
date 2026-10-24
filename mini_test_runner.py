test_cases = [
    {
        "name": "Login Test",
        "expected": "Login successful",
    },
    {
        "name": "Logout Test",
        "expected": "Logout successful",
    },
    {
        "name": "Search Test",
        "expected": "Search successful",
    }
]

def run_test(test_name):
    if test_name == "Login Test":
        actual = "Login successful"
    elif test_name == "Logout Test":
        actual = "Logout successful"
    elif test_name == "Search Test":
        actual = "Search failed"
    else: 
        actual = "unknown test"
    return actual

def check_result(actual, expected):
    if actual == expected:
        result = "PASS"
    else:
        result = "FAIL"
    return result

for test_case in test_cases:
    actual_result = run_test(test_case["name"])
    test_result = check_result(actual_result, test_case["expected"])
    print("=========================")
    print("Running: ", test_case["name"])
    print("Expected: ", test_case["expected"])
    print("Actual: ", actual_result)
    print("Result: ", test_result)


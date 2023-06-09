'''
Name:
SID:
Unikey:
'''

'''
Do not edit the following line - it is required to pass the testcases.
In your test suite, write tests targeting this function.
The function can be called like normal functions, e.g. is_valid_credit_hour()
'''
from program import is_valid_credit_hour

# Write your test cases here
def test_valid_1():
    assert is_valid_credit_hour("3") == True

def test_valid_2():
    assert is_valid_credit_hour("5") == True

def test_negative_1():
    assert is_valid_credit_hour("0") == False

def test_negative_2():
    assert is_valid_credit_hour("6") == False

def test_edge_1():
    assert is_valid_credit_hour("1") == True

def test_edge_2():
    assert is_valid_credit_hour("5") == True

# Run the tests and check if all passed
def run_tests():
    try:
        test_valid_1()
        test_valid_2()
        test_negative_1()
        test_negative_2()
        test_edge_1()
        test_edge_2()
        return True
    except AssertionError:
        return False

# Run the test suite
passed = run_tests()

# Print the result
if passed:
    print("is_valid_credit_hour has passed.")
else:
    print("is_valid_credit_hour has failed.")

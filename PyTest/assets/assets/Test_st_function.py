# function level set up and tear down
# these run before and after each test function
# set up at function level
def setup_function(function):
    print("Opening the browser")

# teardown up at function level
def teardown_function(function):
    print("Closing the browser")

def testcase1():
    print("Testcase1 is executed")
# testcase 2
def testcase2():
    print("Testcase2 is executed")
# testcase 3
def testcase3():
    print("Testcase3 is executed")
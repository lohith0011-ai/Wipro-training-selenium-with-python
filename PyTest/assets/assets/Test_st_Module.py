# module level - runs once per module (file)
# use module level set up and tear down when you want to execute the set up and tear down once in the current file
# eg open the db connection execute all the testcases and at alst close the db connection
# setup_module - -> only one per file
# setup_class() → one per class
# setup_method() → one per class
# setup_function() → one per class
import pytest
def setup_module(module):
    print("Open the db connection")
def teardown_module(module):
    print("Closing the db connection")

# testcase 1
def test_read():
    print("Reading the db")
# testcase 2
def test_write():
    print("Writing the data to db")
# testcase 3
def test_updating():
    print("Updating the db")


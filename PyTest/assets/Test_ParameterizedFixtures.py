import pytest

# request - pytest object that contains information about
# who is calling the fixtures and with what data

@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    print("Current browser:", request.param)
    return request.param

def testbrowser(browser):
    assert browser in ["chrome", "firefox"]
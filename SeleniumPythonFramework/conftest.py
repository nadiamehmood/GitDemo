import pytest

# @pytest.fixture()  # it will run before and after the execution of methods
@pytest.fixture(scope="class")    # it will run before and after the execution of a class
def setup():
    print("I will be executed first")
    yield
    print("i will be executed last")

@pytest.fixture()
def dataLoad():
    print("fixture called")
    return ["nadia", "mehmood", "nadiamehmood66@gmail.com"]


@pytest.fixture(params=[("chrome", "fantastic browser"), ("Firefox", "nadia"), ("IE", "mehmood")])
def crossBrowse(request):     # parameterizing test with multiple data sets using fixtures
    return request.param




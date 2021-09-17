# What are fixtures?
# In general, you have some setup method which you want to run before or after execute tests
# Fixtures are used as setup and tear down methods for test cases
# Fixtures will also help you to load the data
# conftest file is used to generalize fixtures and make it available for all test cases

import pytest

# @pytest.fixture()
# def setup():
#     print("I will be executed first")
#     yield
#     print("i will be executed last")


@pytest.mark.usefixtures("setup")
class TestClass:

    def test_fixtureDemo(self):
        print("I will be executed after fixture")

    def test_fixtureDemo1(self):
        print("I will be executed after fixture")

    def test_fixtureDemo2(self):
        print("I will be executed after fixture")

    def test_fixtureDemo3(self):
        print("I will be executed after fixture")
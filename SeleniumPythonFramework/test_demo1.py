# ---Naming conventions to follow for Pytest Tests:---
# Any pytest file should start with test_
# pytest method names should start with test
# Any code should be wrapped in methods
# ---Running pytest from command line and pycharm:---
# How to get pytest test runner?
# 1. Go to Edit Configurations
# 2. Go to add new configuration by clicking '+' btn
# 3. Click on pytest 4. click on Browse 5. Select that file and press ok
# After these steps "Empty script" error occurred then run this in terminal ->pip3 install pytest-cov
# Run pytest from terminal:
# Run all test cases:
# 1. copy the path from python package and run on cmd "cd C:\Users\Southville\PycharmProjects\CourseTraining\SeleniumPythonFramework"
# 2. run py.test and py.test -v -> V stands for verbose it gives more details in test results
# 3. when you want to run all test cases in 1 single shot with logs details -> py.test -v -s
# -k stands for methods names execution, -s stands for logs in output, -v more info just like meta deta
# ---Running selected test files using pytest:---
# Run specific text case:
# 1. change the path to that directory on terminal-> cd copyPath then run this command
# 2. py.test <fileName>.py -v -s
# ---Running selected test methods based on matching keywords:---
# Run specific test held on 2 different files
# 1. py.test -k regularExpression -v -s -> regularExpression is common keyword for example "firstProgram"
# ---Pytest tags mechanism to run tests based on functionality:---
# 1. Give methods a tag -> @pytest.mark.<whatever name you want to give>
# 2. run this command -> py.test -m smoke -v -s
# ---Failing and skipping tests with Annotations using pytest:---
# 1. define this above that method you want to skip/partially skip -> @pytest.mark.skip -> @pytest.mark.xfail
# 2. then run this on terminal -> py.test -v -s
import pytest


def test_firstProgram(setup):
    print("first program")

# @pytest.mark.smoke
@pytest.mark.xfail # it will run but not report on logs that it fails
def test_Greet():
    print("Good morning")

@pytest.mark.usefixtures("crossBrowse")
def test_crossBrowse(crossBrowse):
    print(crossBrowse)         # prints ('chrome', 'fantastic browser') , ('Firefox', 'nadia') , ('IE', 'mehmood')
    # print(crossBrowse[1])    # prints "fantastic browser" , "nadia" , "mehmood"





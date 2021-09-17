# dataDriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end
import pytest

from SeleniumPythonFramework.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestFixture2(BaseClass):

    def test_profile(self, dataLoad):   # when you return something then you will parameterize fixture like this
        log = self.getLogger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        log.info(dataLoad[2])
        # print(dataLoad[0])
        # print(dataLoad[1])
        # print(dataLoad[2])



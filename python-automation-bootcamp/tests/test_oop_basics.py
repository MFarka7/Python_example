import pytest
from oop_basics import BaseTest


class PassingTest(BaseTest):
    def execute(self):
        self.add_step_result("First passing step","OK","OK")
        self.add_step_result("Second passing step", "OK","OK")


class FailingTest(BaseTest):
    def execute(self):
        self.add_step_result("First passing step", "OK","OK")
        self.add_step_result("Second failiung step","OK","NOK")


class EmptyTest(BaseTest):
    def execute(self):
        pass

class ErrorTest(BaseTest):
    def execute(self):
        self.add_step_result("First step", "OK", "OK")
        raise ConnectionError("API is unavailable")


def test_passing_test():
    test=PassingTest("Test-001","PassingExample")

    assert test.run()=="PASSED"

def test_failing_test():
    test=FailingTest("Test-002","Failing Test")

    assert test.run()=="FAILED"

def test_empty_test():
    test=EmptyTest("Test-003", "Empty test")

    assert test.run()=="INVALID"

def test_error_test():
    test=ErrorTest("Test-004","Error test")

    with pytest.raises(ConnectionError, match="API is unavailable"):
        test.run()

    assert test.status=="ERROR"

@pytest.mark.parametrize("test,expected_status",
    [
        (PassingTest("Scenario 1", "Passing Test"),"PASSED"),
        (FailingTest("Scenario 2", "Failing Test"),"FAILED"),
        (EmptyTest("Scenario 3", "Empty test"),"INVALID")

    ])
def test_parametrization(test,expected_status):
    assert test.run()==expected_status
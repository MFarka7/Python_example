from oop_basics import BaseTest


class PassingTest(BaseTest):
    def execute(self):
        self.add_step_result("First passing step","OK","OK")
        self.add_step_result("Second passing step", "OK","OK")


class FailingTest(BaseTest):
    def execute(self):
        self.add_step_result("First passing step", "OK","OK")
        self.add_step_result("Second failiung step","OK","NOK")


def test_passing_test():
    test=PassingTest("Test-001","PassingExample")

    assert test.run()=="PASSED"

def test_failing_test():
    test=FailingTest("Test-002","Failing Test")

    assert test.run()=="FAILED"
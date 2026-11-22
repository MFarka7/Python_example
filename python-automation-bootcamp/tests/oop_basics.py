from abc import ABC, abstractmethod


class BaseTest(ABC):
    def __init__(self, test_id, name):
        self.name = name
        self.test_id = test_id
        self.status = "NOT STARTED"
        self.steps = []

    def add_step_result(self, step_name, expected, actual): 
       

        self.steps.append({
            "name": step_name,
            "expected": expected,
            "actual": actual,
            "passed": expected==actual
        })


    def run(self):
        self.status="RUNNING"
        try:
            self.execute()
        except Exception as e:
            self.status="ERROR"
            print(f"Test execution issue {e}")
            raise
        else:
            if not self.steps:       
                self.status="INVALID"
            elif self.steps and all(step["passed"] for step in self.steps):
                self.status="PASSED"
            else:
                self.status="FAILED"
            
            return self.status #"why this is in else"



    @abstractmethod
    def execute(self):
        pass

class APITest(BaseTest):
    def __init__(self, test_id, name, endpoint):
        super().__init__(test_id, name)
        self.endpoint = endpoint

    def execute(self):
        # Simulate an API call and check the response
        response = self.mock_api_call(self.endpoint)
        # Check status_code
        self.add_step_result("API Call - Header", 200, response["status_code"])
        # Check status
        self.add_step_result("API Call - Status", "success", response["body"]["status"])


    def mock_api_call(self, endpoint):
        # This is a mock function to simulate an API 
        print(f"Calling endpoint: {endpoint}")
        return {
            "status_code":200,
            "body":{            
                "status": "success"}
        }


class UITest(BaseTest):
    def execute(self):
        self.add_step_result("Open login page", "OK", "OK")
        self.add_step_result("Click login button", "OK", "OK")
        self.add_step_result("Verify dashboard", "visible", "not visible")

class JIRAReporter:
    def __init__(self):
        pass

    def publish(self, test_case:BaseTest):
        print("Publishing test results to JIRA ...")

        print(f"Test ID: {test_case.test_id}")
        print(f"Test Name: {test_case.name}")
        print(f"Status: {test_case.status}")
        print()
        print("Steps: ")
        for step in test_case.steps:
            if step["passed"]:
                step_result="PASSED"
            else:
                step_result="FAILED"
            print("-" + step["name"] + ": " + step_result)
        print()


def main():
    tests = [
        APITest("API-001", "Login API", "/api/login"),
        UITest("UI-001", "Login UI")
    ]

    reporter=JIRAReporter()
    for test in tests:
        test.run()
        reporter.publish(test)


if __name__=="__main__":
    main()
    #nothing to do
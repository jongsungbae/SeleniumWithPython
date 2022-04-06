import os, unittest
from HtmlTestRunner import HTMLTestRunner
from tc_signUp import SignUpTest
from tc_signIn import SignInTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from search Test and homepage Test
signup_test = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
signin_test = unittest.TestLoader().loadTestsFromTestCase(SignInTest)
# create a test suite combining search_test and homepage test
smoke_tests = unittest.TestSuite([signup_test, signin_test])

# configure HTMLTestRunner options
runner = HTMLTestRunner(
    output='smokeTest'
)

# Run the suite using HTMLTestRunner
runner.run(smoke_tests)

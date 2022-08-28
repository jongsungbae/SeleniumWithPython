import os, unittest
from HtmlTestRunner import HTMLTestRunner
from small_project_03.Tests.ecom_test import EcommerceTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from search Test and homepage Test
login_test = unittest.TestLoader().loadTestsFromTestCase(EcommerceTest)

# create a test suite combining search_test and homepage test
smoke_tests = unittest.TestSuite([login_test])

# configure HTMLTestRunner options
runner = HTMLTestRunner(
    output='../Reports'
)

# Run the suite using HTMLTestRunner
runner.run(smoke_tests)

import os, unittest
from HtmlTestRunner import HTMLTestRunner
from small_project_04.Tests.test_login import LoginTest
from small_project_04.Tests.test_create_account import CreateAccountTest
from small_project_04.Tests.test_search_product import SearchProductTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from search Test and homepage Test
login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
create_account_test = unittest.TestLoader().loadTestsFromTestCase(CreateAccountTest)
search_product_test = unittest.TestLoader().loadTestsFromTestCase(SearchProductTest)

# create a test suite combining search_test and homepage test
smoke_tests = unittest.TestSuite([login_test, create_account_test, search_product_test])

# configure HTMLTestRunner options
runner = HTMLTestRunner(output="../Reports")

# Run the suite using HTMLTestRunner
runner.run(smoke_tests)
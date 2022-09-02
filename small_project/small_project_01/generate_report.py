import os, unittest
from HtmlTestRunner import HTMLTestRunner
from GoogleSearchTest import GoogleSearchTest

# get the directory path to output report file
dir = os.getcwd()

# get all tests from search Test and homepage Test
google_search_test = unittest.TestLoader().loadTestsFromTestCase(GoogleSearchTest)

# create a test suite combining search_test and homepage test
smoke_tests = unittest.TestSuite([google_search_test])

# configure HTMLTestRunner options
runner = HTMLTestRunner(output="reports")

# Run the suite using HTMLTestRunner
runner.run(smoke_tests)

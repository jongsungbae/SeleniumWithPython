import os, unittest
from HtmlTestRunner import HTMLTestRunner
from unittest import PfcUnitTest

dir = os.getcwd()

PFC_unit_test = unittest.TestLoader().loadTestsFromTestCase(PfcUnitTest)

smoke_tests = unittest.TestSuite([PFC_unit_test])

runner = HTMLTestRunner(
    output='smokeTest'
)

runner.run(smoke_tests)

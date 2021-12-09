from unittest import TestLoader, TestSuite
#"HTMLTestRunner-rv"
from HTMLTestRunner import HTMLTestRunner
import tests.google_test


test1 = TestLoader().loadTestsFromTestCase(tests.google_test.serachtest)


suite = TestSuite([test1]) #, separated list of tests

runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport")

runner.run(suite)
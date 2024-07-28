import unittest
import HtmlTestRunner

from tests import test_signup, test_login, test_product_browsing, test_add_to_cart, test_logout

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_signup))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_login))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_product_browsing))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_add_to_cart))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(test_logout))

    runner = HtmlTestRunner.HTMLTestRunner(output='reports', report_name='All Tests Report', combine_reports=True)
    runner.run(suite)

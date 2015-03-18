import unittest

from pyfiles.Test.suite import suite as pyfiles_suite

# Collect all the test suites
suites = [pyfiles_suite]

alltests = unittest.TestSuite(suites)

# Run all the tests
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(alltests)

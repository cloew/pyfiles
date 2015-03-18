import unittest

from pyfiles.Test.leading_whitespace_test import suite as leading_whitespace_suite

suites = [leading_whitespace_suite]
suite = unittest.TestSuite(suites)
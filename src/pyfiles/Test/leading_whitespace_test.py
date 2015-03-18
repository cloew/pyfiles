import unittest

from pyfiles.leading_whitespace import LeadingWhitespace

class lessThan(unittest.TestCase):
    """ Test cases of lessThan """
        
    def lessThan(self):
        """ Test that the less than operator works when other is greater """
        whitespaceAmount = 4
        smaller = LeadingWhitespace(" "*whitespaceAmount)
        larger = LeadingWhitespace(" "*(whitespaceAmount+2))
        self.assertTrue(smaller < larger)
        
    def equal(self):
        """ Test that the less than operator works when other is equal """
        whitespaceAmount = 4
        first = LeadingWhitespace(" "*whitespaceAmount)
        second = LeadingWhitespace(" "*whitespaceAmount)
        self.assertFalse(first < second)
        
    def greaterThan(self):
        """ Test that the less than operator works when other is less """
        whitespaceAmount = 4
        smaller = LeadingWhitespace(" "*whitespaceAmount)
        larger = LeadingWhitespace(" "*(whitespaceAmount+2))
        self.assertFalse(larger < smaller)

# Collect all test cases in this class
testcasesLessThan = ["lessThan", "equal", "greaterThan"]
suiteLessThan = unittest.TestSuite(map(lessThan, testcasesLessThan))

##########################################################

class equals(unittest.TestCase):
    """ Test cases of equals """
        
    def lessThan(self):
        """ Test that the equals operator works when other is greater """
        whitespaceAmount = 4
        smaller = LeadingWhitespace(" "*whitespaceAmount)
        larger = LeadingWhitespace(" "*(whitespaceAmount+2))
        self.assertFalse(smaller == larger)
        
    def equal(self):
        """ Test that the equals operator works when other is equal """
        whitespaceAmount = 4
        first = LeadingWhitespace(" "*whitespaceAmount)
        second = LeadingWhitespace(" "*whitespaceAmount)
        self.assertTrue(first == second)
        
    def greaterThan(self):
        """ Test that the equals operator works when other is less """
        whitespaceAmount = 4
        smaller = LeadingWhitespace(" "*whitespaceAmount)
        larger = LeadingWhitespace(" "*(whitespaceAmount+2))
        self.assertFalse(smaller == larger)

# Collect all test cases in this class
testcasesEquals = ["lessThan", "equal", "greaterThan"]
suiteEquals = unittest.TestSuite(map(equals, testcasesEquals))

##########################################################

class add(unittest.TestCase):
    """ Test cases of add """
    WHITESPACE = "    "
    
    def setUp(self):
        """ Build the LeadingWhitespace for the test """
        self.whitespace = LeadingWhitespace(self.WHITESPACE)
        
    def whitespaceAdded(self):
        """ Test that the whitespace is added to the string """
        OTHER = "some random text"
        result = self.whitespace+OTHER
        self.assertEqual("{0}{1}".format(self.WHITESPACE, OTHER), result)

# Collect all test cases in this class
testcasesAdd = ["whitespaceAdded"]
suiteAdd = unittest.TestSuite(map(add, testcasesAdd))

##########################################################

# Collect all test cases in this file
suites = [suiteLessThan,
          suiteEquals,
          suiteAdd]
suite = unittest.TestSuite(suites)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)
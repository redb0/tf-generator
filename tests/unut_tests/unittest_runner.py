import unittest

from tests.unut_tests.generate_func_test import GenerateFuncTestCase
from tests.unut_tests.parser_test import ParserTestCase
from tests.unut_tests.validator_test import ValidationTestCase


def suite():
    unit_test_suite = unittest.TestSuite()
    unit_test_suite.addTest(unittest.makeSuite(GenerateFuncTestCase))
    unit_test_suite.addTest(unittest.makeSuite(ParserTestCase))
    unit_test_suite.addTest(unittest.makeSuite(ValidationTestCase))
    return unit_test_suite


def main():
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())

if __name__ == '__main__':
    main()

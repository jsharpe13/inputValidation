import unittest
from input_validation.validation_with_try import average


class FunctionTestCase(unittest.TestCase):
    def test_average_exception(self):
        with self.assertRaises(ValueError):
            average(-90, 89, 78)

    def test_average_exceptionTwo(self):
        with self.assertRaises(ValueError):
            average(90, -89, 78)

    def test_average_exceptionThree(self):
        with self.assertRaises(ValueError):
            average(90, 89, -78)


if __name__ == '__main__':
    unittest.main()

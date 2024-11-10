import unittest
from math_quiz import get_random_integer, get_random_operator, calculate_expression


class TestMathQuizFunctions(unittest.TestCase):
    """
    Test suite for functions in math_quiz.py.

    This test suite includes:
        - Tests for get_random_integer to check it returns values within a specified range.
        - Tests for get_random_operator to ensure it returns one of the expected operators.
        - Tests for calculate_expression to verify correct calculations based on operators.
    """

    def test_get_random_integer(self):
        """
        Test get_random_integer function.

        Ensures that the function returns an integer within the specified range (inclusive).
        """
        min_value = 1  # Minimum value for the test range
        max_value = 10  # Maximum value for the test range
        result = get_random_integer(min_value, max_value)

        # Assert that result is within the specified range
        self.assertGreaterEqual(result, min_value, "Result should be greater than or equal to minimum value")
        self.assertLessEqual(result, max_value, "Result should be less than or equal to maximum value")

    def test_get_random_operator(self):
        """
        Test get_random_operator function.

        Ensures that the function returns one of the valid operators: +, -, *.
        """
        valid_operators = ['+', '-', '*']  # List of expected operators
        result = get_random_operator()

        # Assert that the result is within the list of valid operators
        self.assertIn(result, valid_operators, "Operator should be in the expected list")

    def test_calculate_expression(self):
        """
        Test calculate_expression function.

        Verifies that the function correctly calculates expressions for the following operators:
            - Addition (+)
            - Subtraction (-)
            - Multiplication (*)

        This test checks both the returned result and the expression format.
        """
        # Test addition
        expression, result = calculate_expression(5, 3, '+')
        self.assertEqual(result, 8, "Addition result should be correct")  # Expecting 5 + 3 = 8
        self.assertEqual(expression, "5 + 3", "Addition expression format should be correct")  # Expression format check

        # Test subtraction
        expression, result = calculate_expression(5, 3, '-')
        self.assertEqual(result, 2, "Subtraction result should be correct")  # Expecting 5 - 3 = 2
        self.assertEqual(expression, "5 - 3",
                         "Subtraction expression format should be correct")  # Expression format check

        # Test multiplication
        expression, result = calculate_expression(5, 3, '*')
        self.assertEqual(result, 15, "Multiplication result should be correct")  # Expecting 5 * 3 = 15
        self.assertEqual(expression, "5 * 3",
                         "Multiplication expression format should be correct")  # Expression format check


# Run the tests when this file is executed
if __name__ == '__main__':
    unittest.main()


import unittest
from math_quiz import get_random_integer, get_random_operator, process_numbers


class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_integer_error(self):
        # Test if failure cases are raises
            test_cases = [
                (-5, -10),
                (5, -10),
                (5.1, 10),
                (5, 10.1),
            ]
            for min_val, max_val in test_cases:
                with self.assertRaises(ValueError):
                    get_random_integer(min_val, max_val)

    def test_get_random_operator(self):
        for _ in range(1000):  # Test a large number of random values
            rand_opr = get_random_operator()
            self.assertTrue(rand_opr in ['+', '-', '*'])

    def test_process_numbers(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (-5, 2, '+', '-5 + 2', -3),
                (-5, 2, '-', '-5 - 2', -7),
                (-5, 2, '*', '-5 * 2', -10),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                received_problem, received_answer = process_numbers(num1, num2, operator)
                self.assertEqual(received_problem, expected_problem)
                self.assertEqual(received_answer, expected_answer)

    def test_process_numbers_error(self):
            test_cases = [
                (-5, 2, '/'),
            ]
            for num1, num2, operator, in test_cases:
                with self.assertRaises(ValueError):
                    process_numbers(num1, num2, operator)

if __name__ == "__main__":
    unittest.main()

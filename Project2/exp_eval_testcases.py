#CPE 202: Project 2 TestCases
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian


# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("19 16 -"), 3)
        self.assertAlmostEqual(postfix_eval("8 4 /"), 2)
        self.assertAlmostEqual(postfix_eval("9 3 *"), 27)
        self.assertAlmostEqual(postfix_eval("5 2 ^"), 25)
        self.assertAlmostEqual(postfix_eval("2 3 2 ^ ^"), 512)

        with self.assertRaises(ValueError):
             postfix_eval("3 0 /")

        try:
           postfix_eval("22 0 /")
        except ValueError as e:
           self.assertEqual(str(e), "Cannot divide by 0")

        self.assertAlmostEqual(postfix_eval("3 4 2 * + 5 -"), 6)
        self.assertAlmostEqual(postfix_eval("3 4 2 * 1 5 - 2 3 ^ ^ / +"), 3.0001220703125)

    def test_postfix_valid(self):
        try:
            postfix_valid("blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid Token")

        with self.assertRaises(PostfixFormatException):
             postfix_valid('string')

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

        with self.assertRaises(PostfixFormatException):
             postfix_valid('231 23 / ^')

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

        with self.assertRaises(PostfixFormatException):
             postfix_valid("64 54 12 ^ 90 / 32 93 8 + 1 55")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )"), "3 4 2 * 1 5 - / +")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"), "3 4 2 * 1 5 - 2 3 ^ ^ / +")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 - 5"), "3 4 2 * + 5 -")        

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("+ 6 3"), "6 3 +")
        self.assertEqual(prefix_to_postfix("+ / - / * 2 7 6 4 2 5"), "2 7 * 6 / 4 - 2 / 5 +")
        self.assertEqual(prefix_to_postfix("- - 3 * 8 12 / 4 2"), "3 8 12 * - 4 2 / -")

if __name__ == "__main__":
    unittest.main()


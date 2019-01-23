#CPE 202 - Lab 2 Test Cases
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian

from perm_lex import*

import unittest

class TestCase(unittest.TestCase):
   def test_perm_lex(self):
       str1 = 'abc'
       self.assertEqual(perm_lex(str1), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
       str2 = 'a' 
       self.assertEqual(perm_lex(str2), ['a'])
       str3 = ''
       self.assertEqual(perm_lex(str3), [])
       self.assertEqual(len(perm_lex('abcde')), 120) 

# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()


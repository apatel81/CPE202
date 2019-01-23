#CPE 202 - Lab 1 Test Cases
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian

from Lab1 import*

import unittest

class TestCase(unittest.TestCase):
   def test_find_max(self):
       list1 = [1,2,3,4]
       list2 = [10, 15, 7, -27]
       list3 = []
       self.assertEqual(find_max(list1), 4)
       self.assertEqual(find_max(list2), 15)
       #self.assertEqual(find_max(list3), 'Empty List')
       self.assertRaises(ValueError) 


   def test_rev_string(self):
       string1 = 'help'
       string2 = ''
       string3 = 'Ajay'
       self.assertEqual(rev_string(string1), 'pleh')
       self.assertEqual(rev_string(string2), '')
       self.assertEqual(rev_string(string3), 'yajA')

   
   def test_bin_search(self):
       list1 = [11, 16, 30, 35, 43]
       list2 = []
       self.assertEqual(bin_search(16,0,4,list1), 1)
       self.assertEqual(bin_search(43,0,4,list1), 4)
       self.assertEqual(bin_search(30,0,4,list1), 2)
       self.assertEqual(bin_search(19,0,4,list1), None)
       self.assertEqual(bin_search(0,0,0,list2), None)

# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()


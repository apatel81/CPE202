#CPE 202 - Lab 4 Test Cases
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian


import unittest
from ordered_list import *

class test_expressions(unittest.TestCase):

      def test_add(self):
          o1 = OrderedList()
          o1.add(1)
          self.assertEqual(o1.add(3), None)
          self.assertEqual(o1.add(2), None)

      def test_remove(self):
          o1 = OrderedList()
          o1.add(1)
          o1.add(2)
          o1.add(3)
          self.assertEqual(o1.remove(3), 2)
          self.assertEqual(o1.remove(2), 1)
          o2 = OrderedList()
          o2.add(1)
          o2.add(2)
          o2.add(3)
          self.assertEqual(o2.remove(2), 1)
     
      def test_search_forward(self):
          o1 = OrderedList()
          o1.add(1)
          o1.add(2)
          o1.add(3)
          self.assertTrue(o1.search_forward(2))
          self.assertFalse(o1.search_forward(5))

      def test_search_backward(self):
          o1 = OrderedList()
          o1.add(1)
          o1.add(2)
          o1.add(3)
          self.assertTrue(o1.search_backward(1))
          self.assertTrue(o1.search_backward(3))
          self.assertFalse(o1.search_backward(5))

      def test_is_empty(self):
          o1 = OrderedList()
          o1.add(1)
          o1.add(2)
          o1.add(3)
          o2 = OrderedList()
          self.assertFalse(o1.is_empty())
          self.assertTrue(o2.is_empty())

      def test_size(self):
          o1 = OrderedList()
          o1.add(1)
          o1.add(2)
          o1.add(3)
          o2 = OrderedList()
          self.assertEqual(o1.size(), 3)
          self.assertEqual(o2.size(), 0)

      def test_index(self):
          o1 = OrderedList()
          o1.add(1)
          o1.add(2)
          o1.add(3)
          self.assertEqual(o1.index(1), 0)
          self.assertEqual(o1.index(2), 1)
          self.assertEqual(o1.index(3), 2)
          self.assertEqual(o1.index(5), -1)

      def test_pop(self):
          o1 = OrderedList()
          o1.add(1)
          o1.add(2)
          o1.add(3)
          self.assertEqual(o1.pop(), 3)
          self.assertEqual(o1.pop(), 2)
          self.assertEqual(o1.pop(), 1)
          o2 = OrderedList()
          o2.add(1)
          o2.add(2)
          o2.add(3)
          self.assertEqual(o2.pop(0), 1)
          self.assertEqual(o2.pop(2), -1)



if __name__ == "__main__":
    unittest.main()

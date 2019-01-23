#CPE 202 - Project 1 Test Cases
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian

from stack_array import*
from stack_linked import*

import unittest

class TestCase(unittest.TestCase):
   
      def test_is_empty(self):
  
          #Tests for Stack Array
          s1 = StackArray(3)
          s3 = StackArray(3)
          s1.push(1)
          s1.push(2)
          s1.push(3)  
          self.assertTrue(StackArray.is_empty(s3))
          self.assertFalse(StackArray.is_empty(s1))
          if 2 in s1:
             print(True)
         
          #Tests for Stack Linked
          s2 = Stack(3)
          s2.push(1)
          s2.push('string')
          self.assertFalse(StackArray.is_empty(s2))
          self.assertTrue(StackArray.is_empty)

      def test_is_full(self):
          
          #Tests for Stack Array
          s1 = StackArray(3)
          s1.push(1)
          s1.push(2)
          self.assertFalse(s1.is_full())
          s2 = StackArray(3)
          s2.push(1)
          s2.push(2)
          s2.push(3)
          self.assertTrue(s2.is_full())

          #Tests for Stack Linked
          s3 = Stack(2)
          s3.push(1)
          s3.push(2)
          self.assertTrue(s3.is_full())
          s4 = Stack(2)
          s4.push('Python')
          self.assertFalse(s4.is_full())

      def test_push(self):

          #Tests for Stack Array
          s1 = StackArray(3)
          s1.push(1)
          s1.push(2)
          self.assertEqual(s1.push(3), None)
          s2 = StackArray(2)
          s2.push(1)
          self.assertEqual(s2.push('Ajay'), None)
          with self.assertRaises(IndexError):
               s2.push('name')          

          #Tests for Stack Linked
          s3 = Stack(2)
          self.assertEqual(s3.push(1), None)
          self.assertEqual(s3.push('dog'), None)   
          with self.assertRaises(IndexError): 
               s3.push('CPE')


      def test_pop(self):

          #Tests for Stack Array
          s1 = StackArray(3)
          s1.push(1)
          s1.push('Patel')
          self.assertEqual(s1.pop(), 'Patel')
          self.assertEqual(s1.pop(), 1)
          s2 = StackArray(3)
          s2.push(1)
          s2.push(2)
          s2.push(3)
          self.assertEqual(s2.pop(), 3)
          self.assertEqual(s2.pop(), 2)
          self.assertEqual(s2.pop(), 1)
          s5 = StackArray(1)
          with self.assertRaises(IndexError):
               s5.pop()

          #Tests for Stack Linked
          s3 = Stack(3)
          s3.push(1)
          self.assertEqual(s3.pop(), 1)
          s3.push(2)
          self.assertEqual(s3.pop(), 2)
          s4 = Stack(3)
          s4.push(1)
          s4.push(2)
          s4.push(3)
          self.assertEqual(s4.pop(), 3)
          self.assertEqual(s4.pop(), 2)
          self.assertEqual(s4.pop(), 1)
          s6 = Stack(1)
          with self.assertRaises(IndexError):
               s6.pop()
 

      def test_peek(self):

          #Tests for Stack Array
          s1 = StackArray(3)
          s1.push(1)
          s1.push(2)
          self.assertEqual(s1.peek(), 2)
          s2 = StackArray(3)
          s2.push(1)
          s2.push(2)
          s2.push(3)
          self.assertEqual(s2.peek(), 3)

          s3 = Stack(3)
          s3.push(1)
          s3.push(2)
          self.assertEqual(s3.peek(), 2)
          s4 = Stack(3)
          s4.push(1)
          self.assertEqual(s4.peek(), 1)

      def test_size(self):
          s1 = StackArray(3)
          s1.push(1)
          s1.push(2)
          self.assertEqual(s1.size(), 2)
          s2 = StackArray(3)
          s2.push(1)
          s2.push(2)
          s2.push(3)
          s2.pop()
          s2.pop()
          self.assertEqual(s2.size(), 1)

          #Tests for Stack Linked
          s3 = Stack(3)
          s3.push(1)
          s3.push(2)
          s3.push(3)
          s3.pop()
          s3.pop()
          self.assertEqual(s3.size(), 1)
          s4 = Stack(3)
          s4.push(1)
          self.assertEqual(s4.size(), 1)


# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()

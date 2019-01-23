#CPE 202 - Lab 3
#Name: Ajay Patel 
#Section: 11
#Instructor: S. Einakian

from queues import*

import unittest

class TestCase(unittest.TestCase):

      def test_is_empty(self):

          #Tests for Queue Array
          q1 = QueueArray(2)
          q1.enqueue(1)
          q1.enqueue('test')
          q2 = QueueArray(2)
          self.assertFalse(q1.is_empty())
          self.assertTrue(q2.is_empty())
          
          #Tests for Queue Linked
          q3 = QueueLinked(2)
          q3.enqueue(1)
          q3.enqueue('test')
          q4 = QueueLinked(2)
          self.assertFalse(q3.is_empty())
          self.assertTrue(q4.is_empty())          


      def test_is_full(self):

          #Tests for Queue Array
          q1 = QueueArray(2)
          q1.enqueue(1)
          q1.enqueue('test')
          q2 = QueueArray(2)
          q2.enqueue(1)
          self.assertTrue(q1.is_full())
          self.assertFalse(q2.is_full())      

          #Tests for Queue Linked
          q3 = QueueLinked(2)
          q3.enqueue(1)
          q3.enqueue('test')
          q4 = QueueLinked(2)
          self.assertTrue(q3.is_full())
          self.assertFalse(q4.is_full())


      def test_enqueue(self):

          #Tests for Queue Array
          q1 = QueueArray(2)
          q1.enqueue(1)
          self.assertEqual(q1.enqueue('test'), None)
          q2 = QueueArray(2)
          q2.enqueue('string')
          q2.dequeue()
          self.assertEqual(q2.enqueue(2), None)
          self.assertEqual(q2.enqueue(1), None)
          self.assertEqual(q2.dequeue(), 2)
          self.assertEqual(q2.enqueue('test'), None)
          with self.assertRaises(IndexError):
               q2.enqueue('name')

          #Tests for Queue Linked
          q3 = QueueLinked(3)
          self.assertEqual(q3.enqueue(1), None)
          q3.enqueue(2)
          q3.dequeue()
          q3.enqueue(34255)
          self.assertEqual(q3.enqueue('Ajay'), None)
          with self.assertRaises(IndexError):
               q3.enqueue('Hope this works')


      def test_dequeue(self):

          #Tests for Queue Array
          q1 = QueueArray(2)
          q1.enqueue(1)
          q1.enqueue('test')
          self.assertEqual(q1.dequeue(), 1)
          q2 = QueueArray(2)
          q2.enqueue(1)
          q2.enqueue(2)
          self.assertEqual(q2.dequeue(), 1)
          self.assertEqual(q2.dequeue(), 2)
          with self.assertRaises(IndexError):
               q2.dequeue()

          #Tests for Queue Linked
          q3 = QueueLinked(2)
          q3.enqueue(1)
          q3.enqueue('test')
          self.assertEqual(q3.dequeue(), 1)
          q4 = QueueLinked(3)
          q4.enqueue(23)
          q4.dequeue()
          with self.assertRaises(IndexError):
               q4.dequeue()


      def test_num_in_queue(self):

          #Tests for Queue Array
          q1 = QueueArray(2)
          q1.enqueue(1)
          q1.enqueue('test')
          self.assertEqual(q1.num_in_queue(), 2)
          q2 = QueueArray(3)
          self.assertEqual(q2.num_in_queue(), 0)

          #Tests for Queue Linked
          q3 = QueueLinked(2)
          q3.enqueue(1)
          q3.enqueue('test')
          q4 = QueueLinked(2)
          self.assertEqual(q3.num_in_queue(), 2)
          self.assertEqual(q4.num_in_queue(), 0)


# Run the unit tests.
if (__name__ == '__main__'):
    unittest.main()




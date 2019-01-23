#CPE 202 - Lab 7 Test Cases
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian

import unittest
from max_heap import *

class test_expressions(unittest.TestCase):

      def test_is_empty(self):
          bh1 = MaxHeap()
          self.assertTrue(bh1.is_empty())
          bh1.insert(5)
          self.assertFalse(bh1.is_empty())   
          bh2 = MaxHeap(3)
          self.assertTrue(bh2.is_empty())
          bh2.insert(1)
          bh2.insert(2)
          self.assertFalse(bh2.is_empty())

      def test_is_empty(self):
          bh1 = MaxHeap()
          bh1.insert(5)
          self.assertFalse(bh1.is_full())
          bh2 = MaxHeap(3)
          bh2.insert(1)
          bh2.insert(2)
          self.assertFalse(bh2.is_full())
          bh2.insert(3)
          self.assertTrue(bh2.is_full())

      def test_insert(self):
          bh1 = MaxHeap()
          self.assertTrue(bh1.insert(10))
          self.assertTrue(bh1.insert(12))
          bh1.insert(23)
          bh1.insert(35)  
          self.assertEqual(bh1.get_heap_size(), 4)

      def test_get_heap_cap(self):
          bh1 = MaxHeap()
          bh1.insert(23)
          bh1.insert(35)
          self.assertEqual(bh1.get_heap_cap(), 50)
          bh2 = MaxHeap(3)
          bh2.insert(1)
          bh2.insert(2)
          bh2.insert(3)
          self.assertEqual(bh2.get_heap_cap(), 3)          
          
      def test_get_heap_size(self):
          bh1 = MaxHeap()
          bh1.insert(23)
          bh1.insert(35)
          self.assertEqual(bh1.get_heap_size(), 2)
          bh2 = MaxHeap(3)
          bh2.insert(1)
          bh2.insert(2)
          bh2.insert(3)
          self.assertEqual(bh2.get_heap_size(), 3)

      def test_find_max(self):
          bh1 = MaxHeap()
          bh1.insert(23)
          bh1.insert(35)
          self.assertEqual(bh1.find_max(), 35)
          bh2 = MaxHeap(3)
          bh2.insert(3)
          bh2.insert(2)
          bh2.insert(1)
          self.assertEqual(bh2.find_max(), 3)

      def test_del_max(self):
          bh1 = MaxHeap()
          bh1.insert(23)
          bh1.insert(35)
          self.assertEqual(bh1.del_max(), 35)
          bh2 = MaxHeap(3)
          bh2.insert(1)
          bh2.insert(2)
          bh2.insert(3)
          self.assertEqual(bh2.del_max(), 3)

      def test_build_heap(self):
          bh1 = MaxHeap()
          list1 = [2, 23, 56, 8, 9, 14]
          self.assertTrue(bh1.build_heap(list1))
          bh2 = MaxHeap(3)
          list2 = [1, 2, 3]
          self.assertTrue(bh2.build_heap(list2))

      def test_heap_contents(self):
          bh1 = MaxHeap()
          list1 = [2, 23, 56, 8, 9, 14]
          bh1.build_heap(list1)
          #print(bh1.get_heap_size())
          self.assertEqual(bh1.heap_contents(), [56, 23, 14, 8, 9, 2])
          bh2 = MaxHeap()
          list2 = [1,2,3,4,5]
          bh2.build_heap(list2)
          self.assertEqual(bh2.heap_contents(), [5,4,3,2,1])
          bh3 = MaxHeap()
          list3 = [11, 51, 17, 9, 23, 30, 5] 
          bh3.build_heap(list3)
          self.assertEqual(bh3.heap_contents(), [51, 30, 17, 9, 23, 11, 5])
 
      def test_heap_sort_increase(self):
          list1 = [23, 56, 8, 9, 14]
          bh1 = MaxHeap()
          self.assertEqual(bh1.heap_sort_increase(list1), [8, 9, 14, 23, 56])
          list2 = [11, 51, 17, 9, 23, 30, 5]
          bh2 = MaxHeap()
          self.assertEqual(bh2.heap_sort_increase(list2), [5, 9, 11, 17, 23, 30, 51]) 



if __name__ == "__main__":
    unittest.main()

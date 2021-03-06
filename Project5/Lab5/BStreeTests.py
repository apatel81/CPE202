#CPE 202 - Lab 5 Test Cases
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian



import unittest
from BStree import *

class test_expressions(unittest.TestCase):

      def test_is_empty(self):
          tree1 = BinarySearchTree()
          self.assertTrue(tree1.is_empty())
          tree1.insert(10)
          tree1.insert(2)
          tree1.insert(13)
          tree1.delete(2)
          self.assertFalse(tree1.is_empty())

      def test_search(self):
          tree1 = BinarySearchTree()
          tree1.insert(10)
          tree1.insert(5)
          tree1.insert(20)
          tree1.insert(2)
          tree1.insert(6)
          tree1.insert(30)
          self.assertTrue(tree1.search(6))
          self.assertTrue(tree1.search(20))
          self.assertFalse(tree1.search(15))
          self.assertTrue(tree1.search(30))

      def test_insert(self):
          tree1 = BinarySearchTree()
          tree1.insert(120)
          self.assertEqual(tree1.insert(12), None)
          self.assertEqual(tree1.insert(24323), None)
          self.assertEqual(tree1.tree_height(), 2)

      def test_delete(self):
          tree1 = BinarySearchTree()
          tree1.insert(10)
          tree1.insert(2)
          tree1.insert(13)
          self.assertEqual(tree1.delete(2), None)
          tree1.insert(44)
          tree1.insert(4)
          tree1.insert(9)
          self.assertEqual(tree1.delete(44), None)
          self.assertEqual(tree1.delete(9), None)

      def test_find_min(self):
          tree1 = BinarySearchTree()
          tree1.insert(10)
          tree1.insert(52)
          tree1.insert(13)
          tree1.insert(4)
          tree1.insert(9)
          self.assertEqual(tree1.find_min(), 4)
          tree2 = BinarySearchTree()
          tree2.insert(5)
          tree2.insert(4)
          tree2.insert(17)
          tree2.insert(20)
          tree2.insert(1)
          self.assertEqual(tree2.find_min(), 1)
          tree3 = BinarySearchTree()
          tree3.insert(10)
          tree3.insert(33)
          self.assertEqual(tree3.find_min(), 10)

      def test_find_max(self):
          tree1 = BinarySearchTree()
          tree1.insert(10)
          tree1.insert(2)
          tree1.insert(13)
          self.assertEqual(tree1.find_max(), 13)
          tree1.insert(44)
          tree1.insert(4)
          tree1.insert(59)
          self.assertEqual(tree1.find_max(), 59)
          tree1.delete(59)
          self.assertEqual(tree1.find_max(), 44)

      def test_inorder_list(self):
          tree1 = BinarySearchTree()
          tree1.insert(10)
          tree1.insert(2)
          tree1.insert(13)
          self.assertEqual(tree1.inorder_list(), [2, 10, 13])
          tree2 = BinarySearchTree()
          tree2.insert(10)
          tree2.insert(20)
          tree2.insert(11)
          tree2.insert(5)
          tree2.insert(1)
          self.assertEqual(tree2.inorder_list(), [1, 5, 10, 11, 20])


      def test_preorder_list(self):
          tree1 = BinarySearchTree()
          tree1.insert(10)
          tree1.insert(2)
          tree1.insert(13)
          self.assertEqual(tree1.preorder_list(), [10, 2, 13])
          tree2 = BinarySearchTree()
          tree2.insert(10)
          tree2.insert(20)
          tree2.insert(11)
          tree2.insert(5)
          tree2.insert(1)
          self.assertEqual(tree2.preorder_list(), [10, 5, 1, 20, 11])


      def test_tree_height(self):
          tree1 = BinarySearchTree()
          tree1.insert(10)
          tree1.insert(2)
          tree1.insert(13)
          self.assertEqual(tree1.tree_height(), 2)
          tree2 = BinarySearchTree()
          tree2.insert(20)
          tree2.insert(11)
          tree2.insert(30)
          tree2.insert(15)
          self.assertEqual(tree2.tree_height(), 3)

if __name__ == "__main__":
    unittest.main()

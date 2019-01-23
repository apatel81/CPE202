#CPE 202 - Lab 8 Test Cases 
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian

import unittest
from sep_chain_ht import *

class test_expressions(unittest.TestCase):

      def test_insert(self):
          ht = MyHashTable()
          ht.insert(1, 'Patel')
          ht.insert(1, 'Ajay')
          ht.insert(2, 'Patel') 
          ht.insert(12, 'Test')
          self.assertEqual(ht.insert(16, 'cat'), None)
          self.assertEqual(ht.insert(37, 'dog'), None)
          print(ht.hash_table)

      def test_get(self):
          ht = MyHashTable()
          ht.insert(1, 'Patel')
          ht.insert(1, 'Ajay')
          ht.insert(2, 'Patel')
          ht.insert(12, 'Test')
          ht.insert(16, 'cat')
          ht.insert(37, 'dog')
          self.assertEqual(ht.get(12), 'Test')
          with self.assertRaises(LookupError):
               ht.get(53)

      def test_remove(self):
          ht = MyHashTable()
          ht.insert(1, 'Patel')
          ht.insert(1, 'Ajay')
          ht.insert(2, 'Patel')
          ht.insert(12, 'Test')
          ht.insert(16, 'cat')
          ht.insert(37, 'dog')
          self.assertEqual(ht.remove(12), (12, 'Test'))
          with self.assertRaises(LookupError):
               ht.remove(53)

      def test_size(self):
          ht = MyHashTable()
          ht.insert(1, 'Patel')
          ht.insert(1, 'Ajay')
          self.assertEqual(ht.size(), 1)
          ht.insert(2, 'Patel')
          ht.insert(12, 'Test')
          ht.insert(16, 'cat')
          ht.insert(37, 'dog')
          self.assertEqual(ht.size(), 5)

      def test_load_factor(self):
          ht = MyHashTable()
          ht.insert(1, 'Patel')
          ht.insert(1, 'Ajay')
          self.assertEqual(ht.load_factor(), 0.09090909090909091)
          ht.insert(2, 'Patel')
          ht.insert(12, 'Test')
          ht.insert(16, 'cat')
          ht.insert(37, 'dog')
          self.assertEqual(ht.load_factor(), 0.45454545454545453)

      def test_collisions(self):
          ht = MyHashTable()
          ht.insert(1, 'Patel')
          ht.insert(1, 'Ajay')
          self.assertEqual(ht.collisions(), 1)
          ht.insert(2, 'Patel')
          ht.insert(12, 'Test')
          ht.insert(16, 'cat')
          ht.insert(37, 'dog')
          ht.insert(48, 'collision')
          self.assertEqual(ht.collisions(), 3)



if __name__ == "__main__":
    unittest.main()

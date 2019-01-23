import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.bicolor())
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.bicolor())

    def test_03(self):
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [['1', '10', '2', '3'], ['6', '7', '8']])
        self.assertFalse(g.bicolor())

    def test_04(self):
        g = Graph('test4.txt')
        self.assertEqual(g.conn_components(), [['1', '2', '3', '4', '5']])
        self.assertTrue(g.bicolor())      


if __name__ == '__main__':
   unittest.main()

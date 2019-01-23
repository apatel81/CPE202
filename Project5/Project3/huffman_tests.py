#CPE 202 - Project 3 Test Cases
#Name: Ajay Patel and Jack Langston
#Section: 11
#Instructor: S. Einakian


import unittest
import filecmp
from huffman import *

class TestList(unittest.TestCase):
   def test_cnt_freq(self):
      freqlist  = cnt_freq("file1.txt")
      anslist = [0]*256
      anslist[97:104] = [2, 4, 8, 16, 0, 2, 0] 
      self.assertListEqual(freqlist[97:104], anslist[97:104])

   def test_create_huff_tree(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      numchars = 32
      charforroot = "a"
      self.assertEqual(hufftree.freq, 32)
      self.assertEqual(hufftree.char, 97)
      left = hufftree.left
      self.assertEqual(left.freq, 16)
      self.assertEqual(left.char, 97)
      right = hufftree.right
      self.assertEqual(right.freq, 16)
      self.assertEqual(right.char, 100)

   def test_create_code(self):
      freqlist = cnt_freq("file1.txt")
      hufftree = create_huff_tree(freqlist)
      codes = create_code(hufftree)
      self.assertEqual(codes[ord('d')], '1')
      self.assertEqual(codes[ord('a')], '0000')
      self.assertEqual(codes[ord('f')], '0001')
      self.assertEqual(codes[ord('c')], '01')
      self.assertEqual(codes[ord('b')], '001')

   def test_01_encodefile(self):
      huffman_encode("file1.txt", "output1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("output1.txt", "output1_soln.txt"))
      huffman_encode("test_sentence.txt", "output3.txt")
      self.assertTrue(filecmp.cmp("output3.txt",'output2.txt'))
      huffman_encode("test_single.txt", "single_output.txt")
      huffman_encode("test_multsingle.txt", "multsingle_output.txt")
      huffman_encode("test_emptyfile.txt", "empty_output.txt")
      huffman_encode("manylines.txt", "manylines_output.txt")

   def test_01_decodefile(self):
      freqlist = cnt_freq("file1.txt")
      huffman_decode(freqlist,"output1.txt", "decodefile1.txt")
      # capture errors by running 'filecmp' on your encoded file
      # with a *known* solution file
      self.assertTrue(filecmp.cmp("decodefile1.txt", "file1.txt"))
      list1 = cnt_freq('test_emptyfile.txt')
      huffman_decode(list1,'empty_output.txt','empty_decode.txt')
      self.assertTrue(filecmp.cmp('empty_decode.txt','test_emptyfile.txt'))
      list2 = cnt_freq('test_single.txt')
      huffman_decode(list2,'single_output.txt','single_decode.txt')
      self.assertTrue(filecmp.cmp('single_decode.txt','test_single.txt'))
      list3 = cnt_freq('test_multsingle.txt')
      huffman_decode(list3,'multsingle_output.txt','multsingledecode.txt')
      self.assertTrue(filecmp.cmp('multsingledecode.txt','test_multsingle.txt'))
      list4 = cnt_freq('manylines.txt')
      huffman_decode(list4, 'manylines_output.txt', 'manylinesdecode.txt')


   def test_tree_preord(self):
       freqlist = cnt_freq("file1.txt")
       hufftree = create_huff_tree(freqlist)
       self.assertEqual(tree_preord(hufftree), ['0','0','0','0','1','a','1','f','1','b','1','c','1','d'])
       self.assertEqual(tree_preord([]), None)
       freqlist2 = cnt_freq("test_emptyfile.txt")
       hufftree2 = create_huff_tree(freqlist2)
       self.assertEqual(tree_preord(hufftree2), None) 
       freqlist3 = cnt_freq("test_single.txt")
       hufftree3 = create_huff_tree(freqlist3)
       self.assertEqual(tree_preord(hufftree3), "1s")
       freqlist4 = cnt_freq("test_multsingle.txt")
       hufftree4 = create_huff_tree(freqlist4)
       self.assertEqual(tree_preord(hufftree4), "1b")
 

if __name__ == '__main__': 
   unittest.main()


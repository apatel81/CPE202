#CPE 202 - Project 3
#Name: Ajay Patel and Jack Langston
#Section: 11
#Instructor: S. Einakian 


import sys
args = sys.argv

class HuffmanNode:

   #initializes the Node
   #character, frequency --> None
   def __init__(self, char, freq):
      #char is a character with a ascii value
      #freq is the freq of the character in the txt file
      #left is the left child of the node
      #right is the right child of the node
      self.char = char  
      self.freq = freq
      self.left = None
      self.right = None

   def set_code(self, code):
      self.code = code

   def set_left(self, node):
      self.left = node

   def set_right(self, node):
      self.right = node

   def isLeaf(self):
      return not (self.left or self.right)

   def hasLeft(self):
      return self.left

   def hasRight(self):
      return self.right




class HuffmanTree:

   #Creates huffman tree
   #None --> None
   def __init__(self):
       #root is a node
       self.root = None


#To check whether node a comes before node b 
#node node --> True or False
def comes_before(a, b) :
    if a.freq < b.freq:
       return True
    elif a.freq == b.freq and ord(a.char) < ord(b.char):
       return True
    else:
       return False    
   

#To count the frequency of strings in file and append frequency to list with ASCII values
#file --> list
def cnt_freq(filename): 
    try:
       file = open(filename, 'r')
    except:
       print("Input file not found")
    empty = []
    file = open(filename, 'r')
    for line in file:
        for elements in line:
            empty.append(elements)

    freq = {}
    for character in empty:
        if not character in freq:        
           freq[character] = 0
        freq[character] += 1

    final_list = [0] * 256    
    for x,y in freq.items(): 
        x = ord(x)
        final_list[x] = y

    return final_list


#To take in a list of 256 ASCII values, convert values > 0 to nodes, and make a Huffman tree from the nodes
#list --> huffman tree
def create_huff_tree(char_freq):
    huff_list = []
    for i in range(len(char_freq)):
        if char_freq[i] > 0:
           node = HuffmanNode(chr(i), char_freq[i])
           huff_list.append(node)

    if len(huff_list) == 0:
       return None

    for node in huff_list:
        node.char = ord(node.char)
      
    while len(huff_list) > 1:
       min1 = find_min(huff_list)
       min2 = findNextMin(huff_list, min1)

       newtree = combine(min1, min2)

       for node in huff_list:
           if node.freq == min1.freq and node.char == min1.char:
              huff_list.remove(node)
           if node.freq == min2.freq and node.char == min2.char:
              huff_list.remove(node)

       huff_list.append(newtree)

    return huff_list[0]


#To find the nodes in the list with the 2 lowest frequencies
#list --> int of min frequency referring to node
def find_min(nodelist):
    minfreq = nodelist[0]
    for node in nodelist:
        if node.freq < minfreq.freq:
           minfreq = node
        elif node.freq == minfreq.freq:
           if (node.char) < (minfreq.char):
              minfreq = node
           
    return minfreq


#To recursivley call find_min without the true min frequency so that the next lowest min is returned
#list(nodes) int(min frequency) --> int of min frequency referring to node
def findNextMin(nodelist, minfreq):
    for node in nodelist:
        if node.freq == minfreq.freq and node.char == minfreq.char:
           nodelist.remove(node)
    return find_min(nodelist)


#To create a new node; frequency = sum of 2 min node frequencies, data = lower ASCII value of 2 min nodes
#node(min 1)  node(min 2)  --> node 
def combine(a, b):
   if (a.char) > (b.char):
      newchar = b.char
   else:
      newchar = a.char
 
   newfreq = a.freq + b.freq
 
   if a.freq > b.freq:
      newleft = b
      newright = a
   elif a.freq == b.freq:
      if (a.char) > (b.char):
         newleft = b
         newright = a
      else:
         newleft = a
         newright = b
   else: 
      newright = b
      newleft = a
 
   newnode = HuffmanNode(newchar,newfreq) #makes new node
   newnode.left = newleft
   newnode.right = newright
   return newnode


#To create a list of the 256 ASCII values so we can append the Huffman leaves 
#string path to corresponding ASCII value; uses a helper function 
#node --> string
def create_code(node):
    coded = [None]*256
    str = ''
    rootfreq = node.freq
    return traverse_tree(node, coded, str, rootfreq)


#To return the string representing path to leaves in Huffman Tree
#node, list of 256 ASCII values, empty string, node frequency
def traverse_tree(node, coded, str, rootfreq):
    if node.isLeaf():
       coded[node.char] = str
       return
    else:
       if node.hasLeft():
          str = str + '0'
          traverse_tree(node.left, coded, str, rootfreq)
          str = str[:-1]
       if node.hasRight():
          str = str + '1'
          traverse_tree(node.right, coded, str, rootfreq)
          str = str[:-1]
       if node.freq != rootfreq:
          return
    return coded


#To write the preorder traversal of our tree
#Node(tree) --> str
def tree_preord(tree):
    prelist = [] 
    return preorder_helper(tree, prelist)

#To actually write the preorder traversal
#node list --> list
def preorder_helper(temp, prelist):
    if not temp:
       return
    
    if temp.isLeaf():
       prelist.append('1')
       prelist.append(chr(temp.char))
    else:
       prelist.append('0')

    preorder_helper(temp.left, prelist)
    preorder_helper(temp.right, prelist)

    if len(prelist) == 2:
       return "".join(prelist)
               
    return prelist


#To convert the ASCII values to 0's and 1's
#in_file and empty out file --> out file
def huffman_encode(in_file, out_file):
    input_list = cnt_freq(in_file)
    count_original = 0
    listed_file = open(in_file,'r')

    file_list = []
    for i in range(len(input_list)):
       if input_list[i] > 0:
          j = i
          count_original += 1

    if count_original == 0:
       out_file = open(out_file, "w")
       out_file.write("")

    elif count_original <= 2:
       out_file = open(out_file, 'w')
       list1 = [chr(j), " " ,input_list[j]]      
       for i in list1:
           out_file.write(str(i))
       return 
    else:
      root = create_huff_tree(input_list)
      final_string = create_code(root)
      out_file = open(out_file, 'w')

      for line in listed_file:
         for character in line:
                 file_list.append(character)

      for i in file_list:      
          code = final_string[ord(i)]
          out_file.write(code)


#To interpret 0s and 1s into strings and or sentences
#list, file, empty file --> file of strings
def huffman_decode(freqs, encoded_file, decode_file):
    try:
       in_file = open(encoded_file, 'r')
    except FileNotFoundError:
       print("Input file not found")
   
    out_file = open(decode_file, "w")
    elements = []
    count = 0
    for line in in_file:
        for element in line:
           count += 1 
           elements.append(element)

    if count == 0:
       out_file.write("")
    elif not elements[0].isdigit():
       for i in range(int(elements[2])):
           out_file.write(elements[0])
    else: 
       hufftree = create_huff_tree(freqs)
       huffnode = hufftree

       for item in elements:    
           if item == '0':
              huffnode = huffnode.left
           if item == '1':
              huffnode = huffnode.right
           if huffnode.isLeaf():
              out_file.write(chr(huffnode.char))
              huffnode = hufftree

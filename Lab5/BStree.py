#CPE 202 - Lab 5 
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian 

class TreeNode:

      def __init__(self, key, data = None, left = None, right = None, parent = None):
          self.key = key 
          self.data = None
          self.left_child = None
          self.right_child = None 
          self.parent = None

      def isRoot(self):
          return not self.parent

      def isLeaf(self):
          return not (self.left_child or self.right_child)

      def hasLeftChild(self):
          return self.left_child

      def hasRightChild(self):
          return self.right_child

      def isLeftChild(self):
          return self.parent and self.parent.left_child == self

      def isRightChild(self):
          return self.parent and self.parent.right_child == self 

      def hasAnyChildren(self):
          return self.left_child or self.right_child

      def hasBothChilden(self):
          return self.left_child and self.right_child

      def hasNoChildren(self):
          return (not self.left_child) and (not self.right_child)

      def hasOneChild(self):
          return (self.left_child and not self.right_child) or (self.right_child and not self.left_child)

      def replaceNodeData(self, key, data, lc, rc):
          self.key = key
          self.data = data
          self.left_child = lc
          self.right_child = rc
          if self.hasLeftChild():
             self.left_child.parent = self
          if self.hasRightChild():
             self.right_child.parent = self

      def insert(self, key):
          if self.key != None:
             if key < self.key:
                if self.left_child is None:
                   self.left_child = TreeNode(key)
                   self.left_child.parent = self
                else:
                   self.left.insert(key)
             elif key > self.key:
                if self.right_child is None:
                   self.right_child = TreeNode(key)
                   self.right_child.parent = self
                else:
                   self.right_child.insert(key)
          else:
             self.key = key


      def inorder_list(self):
          if self.left_child is not None:
             self.left_child.inorder_list()

          print(self.key)

          if self.right_child is not None:
             self.right_child.inorder_list()


      #To return a list of the BST keys pre order traversal
      #None --> list
      def preorder_list(self):
          empty_list = []

          print(self.key)

          if self.left_child is not None:
             self.left_child.preorder_list()

          if self.right_child is not None:
             self.right_child.preorder_list()



class BinarySearchTree:

      #To return an empty BST
      #None --> None
      def __init__(self):
          self.root = None
          self.size = 0
          self.temproot = None


      #To see if the tree is empty 
      #None --> True if empty; False if not empty 
      def is_empty(self):
          if self.root == None:
             return True
          else:
             return False


      #To see if a key is in the tree
      #key --> True if in tree; False if not in tree
      def search(self, key):
          if self.root:
             res = self.get(key, self.root)
             if res:
                return True
             else:
                return False
          else:
             return False


      #Helper function to search
      #int node --> True or False
      def get(self, key, currentNode):
          if not currentNode:
             return None
          elif currentNode.key == key:
             return currentNode
          elif key < currentNode.key:
             return self.get(key, currentNode.left_child)
          else:
             return self.get(key, currentNode.right_child)


      #To insert a new node with a key and data 
      #key --> None
      def insert(self, key):
          if self.root == None:
             self.root = TreeNode(key)
             return
          else:
             temproot = self.root
             if key < temproot.key:
                if temproot.left_child is None:
                   temproot.left_child = TreeNode(key)
                   temproot.left_child.parent = temproot
                else:
                   temproot.left_child.insert(key)
             else:
                if temproot.right_child is None:
                   temproot.right_child = TreeNode(key)
                   temproot.right_child.parent = temproot
                else:
                   temproot.right_child.insert(key)

          self.size += 1


      #To delete a node containing an existing key 
      #key --> None
      def delete(self, key):
          current = self.root
          while current.key != key:
             if current.key > key:
                current = current.left_child
             else:
                current = current.right_child
          if current.hasNoChildren():
             if current == self.root:
                self.root = None
             elif current == current.parent.left_child:
                current.parent.left_child = None 
             else:
                current.parent.right_child = None 
          elif current.hasOneChild():
             if current.right_child:
                if current == self.root:
                   current.right_child.parent = current.parent
                   current.parent.right_child = current.right
             elif current.left_child:
                if current == self.root:
                   current.left_child.parent = None 
                   self.root = current.left_child
          else:
             current_new = current.right_child.find_min()
             current.key = current_new.key
             if current_new.parent.left_child == current_new:
                current_new.parent.left_child = None
             else:
                current_new.parent.right_child = None


      #Helper function to remove
      #None --> Node
      def find_successor(self):
          successor = None
          if self.hasRightChild():
             successor = self.right_child.find_min()
          else:
             if self.parent:
                if self.isLeftChild():
                   successor = self.parent
                else:
                   self.parent.right_child = None
                   successor = self.parent.find_successor()
                   self.parent.right_child = self
          return successor


      #To return the node with the lowest key in BST
      #None --> key
      def find_min(self):
          temp = self.root
          while temp.left_child != None:
                temp = temp.left_child
          return temp.key


      #To return the node with the largest key in BST 
      #None --> key
      def find_max(self):
          temp = self.root
          while temp.right_child != None:
                temp = temp.right_child
          return temp.key


      #To return a list of the BST keys in order traversal
      #None --> list
      def inorder_list(self):
          empty_list = []

          return self.inorder_helper(self.root, empty_list)

      #To help inorder_list create a list of keys
      #root, empty list --> list with keys
      def inorder_helper(self, temp, empty_list):
          if not temp:
             return 
          self.inorder_helper(temp.left_child, empty_list)
          empty_list.append(temp.key)
          self.inorder_helper(temp.right_child, empty_list) 
          return empty_list


      #To return a list of the BST keys pre order traversal
      #None --> list
      def preorder_list(self):
          empty_list = []

          return self.preorder_helper(self.root, empty_list)

      #To help preorder_list make a list of keys
      #root, empty list --> list with keys
      def preorder_helper(self, temp, empty_list):
          if not temp:
             return
          empty_list.append(temp.key)
          self.preorder_helper(temp.left_child, empty_list)
          self.preorder_helper(temp.right_child, empty_list)
          return empty_list

      #To return the height of the BST
      #None --> int
      def tree_height(self):
          if self.root is None:
             return 0
          else:
             temp = self.root
             left_height = 0
             while temp.left_child != None:
                left_height += 1
                temp = temp.left_child
                if temp.hasLeftChild():
                   temp = temp.left_child
                   left_height += 1
                elif temp.hasRightChild():
                   temp = temp.right_child
                   left_height += 1

             right_height = 0
             while temp.right_child != None:
                right_height += 1
                temp = temp.right_child
                if temp.hasLeftChild():
                   temp = temp.left_child
                   right_height += 1
                elif temp.hasRightChild():
                   temp = temp.right_child
                   right_height += 1

          if left_height > right_height:
             return left_height + 1
          else:
             return right_height + 1



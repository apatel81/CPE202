#CPE 202 - Lab 4
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian


class Node:
     def __init__(self, newval):
         self.value = newval
         self.next = None
         self.previous = None
     def __repr__(self):
         return self.value


class OrderedList:
     def __init__(self):
         self.head = None
         self.tail = None
         self.num_items = 0 


     #To add a item to the list in order
     #int --> None
     def add(self, item):
         temp = Node(item)
         current = self.head
         previous = None 
         stop = False
         while current != None and not stop:
               if current.value > item:
                  stop = True
               else:
                  previous = current 
                  current = current.next
                 
         if previous == None:
            temp.next = self.head
            self.head = temp
            self.tail = temp
 
         else:
            temp.next = self.head
            self.head.previous = temp
            temp.previous = None
            self.head = temp
                     
         self.num_items += 1

     #To remove a item from the list
     #item --> index(item) or -1 if not found 
     def remove(self, item):
         current = self.head
         previous = None
         found = False
         count = self.num_items - 1 
         while not found and count >= 0:
            if current.value == item:
               found = True
            else:
               previous = current
               current = current.next 
               count -= 1

         if previous == None:
            self.head = current.next
         else:
            previous.next = current.next

         self.num_items -= 1
         if found == False:
            return -1
         else:
            return count

     #To search, in the forward direction, for an item
     #item --> True or False
     def search_forward(self, item):
         if self.head is None:
            return False
         current = self.head
         while current is not None:
               if current.value == item:
                  return True
               else:
                  current = current.next
         return False


     #To search, in the backward direction, for an item
     #item --> True or False
     def search_backward(self, item):
         if self.tail is None:
            return False
         current = self.tail
         while current is not None:
               if current.value == item:
                  return True
               else:
                  current = current.previous
         return False

     #To see whether or not the list is empty 
     #None --> True(empty) or False(not empty)
     def is_empty(self):
         if self.num_items == 0:
            return True
         else: 
            return False

     #To tell us the number of items in the list
     #None --> int
     def size(self):
         return self.num_items


     #To tell us the index of an item in the list
     #item --> int(index) or -1 if item not found
     def index(self, item):
         found = False
         index_count = self.num_items - 1
         if self.head is None:
            return -1
         current = self.head
         while current is not None and not found:
               if current.value == item:
                  found = True
               else:
                  current = current.next
                  index_count -= 1         

         if found == False:
            return -1
         else:
            return index_count

     #To remove the last item in the list or remove an item from a certain index
     #None or index --> item
     def pop(self, pos = None):
         if pos == None:
            current = self.head
            self.head = current.next
            self.num_items -= 1
            return current.value

         else:
            count = 0
            item = self.num_items - 1
            if pos > (self.num_items - 1):
               return -1
            elif pos < 0:
               return -1
            elif pos <= (self.num_items//2):
               while count <= (self.num_items//2):
                  if count == pos:
                     current = self.tail
                     self.tail = current.previous
                     self.num_items -= 1
                     return current.value
                  else:
                     count += 1
          
            elif pos > (self.num_items//2):
               while item > (self.num_items//2):
                  if item == pos:
                     current = self.head
                     self.head = current.next
                     self.num_items -= 1
                     return current.value
                  else:
                     item -= 1
            else:
               return -1

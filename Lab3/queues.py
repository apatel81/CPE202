#CPE 202 - Lab 3
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian 

class QueueArray:
   #To initialize the class QueueArray
   #int --> None
   def __init__(self, capacity):
      self.capacity = capacity
      self.front = 0
      self.rear = 0
      self.size = 0 
      self.items = [None] * capacity


   #To tell us whether or not the Queue is empty 
   #None --> True if empty and False if not empty
   def is_empty(self):
       if self.size == 0:
          return True
       else: 
          return False 


   #To tell us whether or not the Queue is full
   #None --> True if full and False if not full
   def is_full(self):
       if self.size == self.capacity:
          return True
       else:
          return False
   

   #To add an item into the Queue
   #item --> None
   def enqueue(self, item):
       if self.size == self.capacity:
          raise IndexError('Queue is full')
       else:
          if self.items[self.rear] == None:
             self.items[self.rear] = item
             if self.size == 0 and self.rear == 0:
                self.front = 0
                self.rear += 1
             elif self.size == 0 and self.rear > 0:
                self.rear += 1
             else:
                self.rear += 1
          self.size += 1
          if self.rear == (self.capacity) and self.size != self.capacity:
             self.rear = 0


   #To remove an item from the Queue
   #None --> item
   def dequeue(self):
       if self.size == 0:
          raise IndexError('Queue is empty')
       else:
          item_dequeue = self.items[self.front]
          self.items[self.front] = None
          self.size -= 1
          if self.front == (self.capacity - 1) and self.size < self.capacity:
             self.front = 0 
          else:
             self.front += 1
     
       return item_dequeue

   #To tell us the number of items in the queue
   #None --> int
   def num_in_queue(self):
       return self.size



class Node:
    #To initialize the class Node
    #int --> None
    def __init__(self, newval):
        self.value = newval
        self.next = None

class QueueLinked:
    #To initialize the class QueueLinked
    #int --> None
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = None
        self.rear = None
        self.size = 0

 
    #To tell us whether or not the Queue is empty
    #None --> True if empty and False if not empty
    def is_empty(self):
        if self.size == 0:
           return True
        else:
           return False


    #To tell us whether or not the Queue is full
    #None --> True if full and False if not full  
    def is_full(self):
        if self.size == self.capacity:
           return True
        else:
           return False

   
    #To push an item into the Queue
    #item --> None
    def enqueue(self, item):
        if self.size == self.capacity:
           raise IndexError('Queue is full')
        else:
           temp = Node(item)
           temp.next = self.front
           if self.size == 0: 
              self.front = temp
              self.rear = temp
           else:
              self.rear = temp
 
           self.size += 1


    #To remove an item from the Queue
    #None --> item
    def dequeue(self):
        if self.size == 0:
           raise IndexError('Queue if empty')
        else:
           temp = self.front.value
           self.front = self.front.next
           self.size -= 1
                      
        return temp

    #To tell us the number of items in the queue
    #None --> int
    def num_in_queue(self):
        return self.size

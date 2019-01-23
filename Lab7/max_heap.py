#CPE 202 - Lab 7 
#Name: Ajay Patel
#Instructor: S. Einakian
#Section: 11


class MaxHeap:


   #initialize the max heap
   #None --> None
   def __init__(self, capacity = 50):
       self.capacity = capacity
       self.size = 0
       self.heaplist = [0]

   
   #To insert an item into the heap 
   #item --> True if inserted, False if no room 
   def insert(self, item):
       if self.size <= self.capacity:
          self.heaplist.append(item)
          self.size += 1
          self.perc_up(self.size)
          return True
       else: 
          return False


   #To insert an item in the heap at the correct location by swapping up values
   #index --> None
   def perc_up(self, i):
       swap = False
       while i//2 > 0:
          if self.heaplist[i] > self.heaplist[i//2]:
             temp = self.heaplist[i]
             self.heaplist[i] = self.heaplist[i//2]
             self.heaplist[i//2] = temp
             swap = True
             if i*2+1 < len(self.heaplist):
                if swap == True:
                   if self.heaplist[i] < self.heaplist[i*2+1]:
                      temp = self.heaplist[i]
                      self.heaplist[i] = self.heaplist[i*2+1]
                      self.heaplist[i*2+1] = temp
             elif i*2 < len(self.heaplist):
                if swap == True:
                   if self.heaplist[i] < self.heaplist[i*2]:
                      temp = self.heaplist[i]
                      self.heaplist[i] = self.heaplist[i*2]
                      self.heaplist[i*2] = temp
          i = i//2 


   #To insert an item in the heap at the correct location by swapping down values
   #index --> None
   def perc_down(self, i):
       swap = False
       while (i * 2) <= self.size:
          mc = self.maxChild(i)
          if self.heaplist[i] > self.heaplist[mc]:
             temp = self.heaplist[i]
             self.heaplist[i] = self.heaplist[mc]
             self.heaplist[mc] = temp
             swap = True
             if i*2+1 < len(self.heaplist):
                if swap == True:
                   if self.heaplist[i] > self.heaplist[i*2+1]:
                      temp = self.heaplist[i] 
                      self.heaplist[i] = self.heaplist[i*2+1]
                      self.heaplist[i*2+1] = temp
             elif i*2 < len(self.heaplist):
                if swap == True:
                   if self.heaplist[i] > self.heaplist[i*2]:
                      temp = self.heaplist[i] 
                      self.heaplist[i] = self.heaplist[i*2]
                      self.heaplist[i*2] = temp
             
          i = mc


   #To find the minimum of the current node's 2 children 
   #index --> index
   def maxChild(self, i):
       if i*2+1 > self.size:
          return i * 2
       else:
          if self.heaplist[i*2] > self.heaplist[i*2+1]:
             return i*2
          else:
             return i*2+1   


   #To find and return the max value in the heap
   #None --> int ; None if heap is empty
   def find_max(self):
       if self.size == 0:
          return None
       else:
          return self.heaplist[1]


   #To remove & return max value in heap and maintain shape and order in max heap
   #None --> int ; None if heap is empty 
   def del_max(self):
       if self.size == 0:
          return None
       else:   
          max_value = self.heaplist[1]
          self.heaplist[1] = self.heaplist[self.size]
          self.size -= 1
          self.heaplist.pop()
          self.perc_down(1)
          return max_value


   #To return a list of the items in the heap in the order it is stored internal to the heap
   #None --> list
   def heap_contents(self):
       my_list = []
       i = 1
       while i < len(self.heaplist):
           my_list.append(self.heaplist[i])
           i += 1
       return my_list
       

   #To build a heap from a list from the bottom up
   #list --> True if build was successful ; False if heap is too large
   def build_heap(self, alist):
       if len(alist) > self.capacity:
          return False
       else:
          #i = len(alist)//2
          i = len(alist)
          self.size = len(alist)
          self.heaplist = [0] + alist[:]
          while i > 0:
             self.perc_up(i)
             i -= 1
          return True


   #To check if the heap is empty
   #None --> True if heap is empty ; False otherwise
   def is_empty(self):
       if self.size == 0:
          return True
       else: 
          return False


   #To check if the heap is full 
   #None --> True if heap is full ; False otherwise 
   def is_full(self):
       if self.size == self.capacity:
          return True
       else:
          return False


   #To return the maximum number of entries the heap can hold
   #None --> int
   def get_heap_cap(self):
       return self.capacity


   #To return the number of elements in the heap
   #None --> int
   def get_heap_size(self):
       return self.size


   #To append the values of a max heap to a list in non-decreasing order
   #list --> list
   def heap_sort_increase(self, alist):
       max_list = [] 
       while len(alist) > 0:
          max_value = max(alist)
          alist.remove(max_value)
          max_list.append(max_value)

       index = len(max_list) - 1
       increase_list = []
       while index >= 0:
           increase_list.append(max_list[index])
           index -= 1
       return increase_list


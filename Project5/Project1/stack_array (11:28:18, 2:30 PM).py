#CPE 202 - Project 1
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian



class StackArray:

    #To create an empty stack with n capacity
    #int --> None
    def __init__(self, capacity):
        self.capacity = capacity                
        self.items = [None]*capacity            
        self.num_items = 0                      

    
    #To check whether the stack is empty or not
    #None --> True or False
    def is_empty(self):
        if self.num_items == 0:
           return True
        else:
           return False

    #To check whether or not the stack is full
    #None --> True if stack is full or False if stack is not full
    def is_full(self):
        if self.num_items == self.capacity:
           return True
        else:
           return False


    #To add item(s) to the stack 
    #item --> None
    def push(self, item):
        if self.num_items == self.capacity:
           raise IndexError('Stack is full')
        else:
           for i in range(0, self.capacity):
               if self.items[i] == None:
                  self.items[i] = item
                  self.num_items += 1
                  break


    #To remove the last item in the array 
    #None --> item in array 
    def pop(self): 
        if self.num_items == 0:
           raise IndexError('Stack is empty')
        else:
           item_pop = self.items[self.num_items - 1]
           self.items[self.num_items - 1] = None
           self.num_items -= 1
        
        return(item_pop) 
              


    #To see what the last item in the array
    #None --> item in array 
    def peek(self):
        if self.num_items == 0:
           raise IndexError('Stack is empty')
        else:
           item_peek = self.items[self.num_items - 1]
      
        return(item_peek)


    #To return the number of items in stack
    #None --> int
    def size(self):
       return(self.num_items)

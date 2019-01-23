#CPE 202 - Project 1
#Name: Ajay Patel
#Section: 1
#Instructor: S. Einakian


class Node:
    def __init__(self, newval):
        self.value = newval
        self.next = None

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.num_items = 0


    #To check whether or not the stack is empty 
    #None --> True if stack is empty and False if stack is not empty
    def is_empty(self):
        if self.num_item == 0:
           return True
        else:
           return False

    #To check whether or not the stack is full
    #None --> True if stack is full and False if stack is not full 
    def is_full(self):
        if self.num_items == self.capacity:
           return True
        else:
           return False         
   
    #To take an item and add it to the stack 
    #item --> None
    def push(self, item):
        if self.num_items == self.capacity:
           raise IndexError('Stack is full')
        else:
           temp = Node(item)
           temp.next = self.head
           self.head = temp
           self.num_items += 1           


    #To remove an item from the stack if the stack is not empty 
    #None --> item 
    def pop(self): 
        if self.num_items == 0:
           raise IndexError('Stack is empty')
        else:
           temp = self.head.value 
           self.head = self.head.next
           self.num_items -= 1

        return temp

    #To return the last item in the stack without removing it 
    #None --> item 
    def peek(self):
        if self.num_items == 0:
           raise IndexError('Stack is empty')
        else:
           item = self.head

        return item.value

    #To get the total number of nodes in the stack
    #None --> int
    def size(self):
        return self.num_items

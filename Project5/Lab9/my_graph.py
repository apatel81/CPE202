#CPE 202 - Lab 9 
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian

from stack_array import*

class MyGraph:

   #To create a graph using an adjacency list by reading an input file
   #filename --> None
   def __init__(self, filename):
       linenumber = 1
       file = open(filename, 'r')
       for line in file:
           if linenumber == 1:
              if len(line) == 1:
                 self.number_of_vertices = int(line)  
                 #print(self.number_of_vertices)
              else:
                 self.number_of_vertices = int(line[0] + line[1])
              linenumber += 1
              self.adjmatrix = [[] for _ in range(int(self.number_of_vertices)+1)]              
           elif linenumber == 2:
              self.number_of_edges = line
              linenumber += 1
           else:
              if len(line) == 4:
                 self.adjmatrix[int(line[0])].append(int(line[2]))
                 self.adjmatrix[int(line[2])].append(int(line[0]))
              if len(line) == 5:
                 self.adjmatrix[int(line[0] + line[1])].append(int(line[3]))
                 self.adjmatrix[int(line[3])].append(int(line[0] + line[1]))  
              linenumber += 1

       #print(self.adjmatrix)
                

   #To return a list of lists representing the vertices that are connected in each list
   #None --> list of lists
   def conn_components(self):
       cclist = []
       vertlist = []
       visitedlist = []
       #my_stack = StackArray(int(self.number_of_vertices))
       for i in range(1, len(self.adjmatrix)):
           if i not in visitedlist:
              my_stack = StackArray(100)
              my_stack.push(i)
              #templist = []
              self.dfs(i, visitedlist, my_stack)

              stacklist = []
              while my_stack.is_empty() is False:
                 tmp = my_stack.pop()
                 vertlist.append(tmp)
                 if tmp not in stacklist:
                    stacklist.append(tmp)
             
              stacklist = sorted(stacklist) 
              cclist.append(stacklist)
    
       for i in range(1, int(self.number_of_vertices) + 1):
           if i not in vertlist:
              cclist.append([i])    

       print(cclist)
       return cclist



   #To recursively do depth first search
   #int(vrtx), list(list of visited vertices), stack
   def dfs(self, idx, visit_list, stack):
       if idx not in visit_list: 
          stack.push(idx)
          visit_list.append(idx)
          for i in range(len(self.adjmatrix[idx])):
              self.dfs(self.adjmatrix[idx][i], visit_list, stack)



g = MyGraph('test.txt')
g.conn_components()

g2 = MyGraph('test2.txt')
g2.conn_components()

g3 = MyGraph('test3.txt')
g3.conn_components()

g4 = MyGraph('test4.txt')
g4.conn_components()



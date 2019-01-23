#CPE 202 - Project 5
#Name: Ajay Patel
#Instructor: S. Einakian
#Section: 11


from stack_array import*
from queues import*


class Vertex:

    #To initialize a Vertex object
    #key --> None
    def __init__(self, key):
        self.id = key
        self.adjacent_to = []


    #To add the adjacent vertices of the current vertex to the adjacent list
    #key --> None
    def add_neighbor(self, v):
        self.adjacent_to.append(v.id)


    #To get all the adjacent vertices
    #None --> list
    def getConnection(self):
        return self.adjacent_to
        

class Graph:

    #To read the input file and create a Graph using the strings in the file
    #file --> Graph object
    def __init__(self, filename):
        self.vertlist = []
        self.number_of_vertices = 0
        file = open(filename, 'r')        
        for line in file:
            index = 0
            vertex1 = ''
            while line[index] != ' ':
               vertex1 += line[index]
               index += 1
            
            vertex2 = ''
            while index < len(line):
               if line[index] == '\n':
                  break
               else:
                  vertex2 += line[index] 
                  index += 1

            vertex1 = vertex1.strip()
            vertex2 = vertex2.strip()
            vertex1 = self.get_vertex(vertex1)         #Makes a vertex object
            vertex2 = self.get_vertex(vertex2)         #Makes a vertex object
            self.add_edge(vertex1.id, vertex2.id)      #Makes connection from 1 to 2
            
        file.close()


    #To add a vertex to the graph
    #key --> None
    def add_vertex(self, id):
        self.number_of_vertices += 1
        self.vertlist.append(self.get_vertex(id))

   
    #To take a key as input and return it as an object of class Vertex
    #int(key) --> Vertex(key)
    def get_vertex(self, key):
        return Vertex(key)


    #To add a connecting vertex (edge) to an existing vertex
    #int int --> None
    def add_edge(self, v1, v2):
        if not self.is_in(v1, self.vertlist):
           self.add_vertex(v1)
        if not self.is_in(v2, self.vertlist):
           self.add_vertex(v2)

        a = self.find_vertex(v1, self.vertlist)  #a is a vertex object 
        b = self.find_vertex(v2, self.vertlist)  #b is a vertex object
        a.add_neighbor(b)
        b.add_neighbor(a)


    #Helper function to find vertex with matching key in vertex list
    #int(vertex id), alist(vertlist) --> vertex object
    def find_vertex(self, key, alist):
        for i in alist:
            if i.id == key:
               return i


    #Helper function to compare vertex object in vertex list
    #int(vertex id) list(vertlist) --> bool
    def is_in(self, key, alist):
        for i in alist:
            if i.id == key:
               return True
        return False    


    #To return the list of vertices in the graph
    #None --> list
    def get_vertices(self):
        return self.vertlist


    #To return a list of lists of the vertices that are connected
    #None --> list
    def conn_components(self): 
        cclist = []
        visitedlist = []
        for v in self.vertlist:
            if v.id not in visitedlist:
               my_stack = StackArray(100)
               self.dfs(v, visitedlist, my_stack)                   

               stacklist = []
               while my_stack.is_empty() is False:
                  tmp = my_stack.pop()
                  stacklist.append(tmp)

               stacklist = sorted(stacklist)
               cclist.append(stacklist)

        return cclist


    #Helper function to perform Depth First Search
    #int(current vrtx), list(visited vertices), stack
    def dfs(self, vrtx, visit_list, stack):
        if vrtx.id not in visit_list:
           stack.push(vrtx.id)
           visit_list.append(vrtx.id)
           for i in vrtx.getConnection():
               a = self.find_vertex(i, self.vertlist)
               self.dfs(a, visit_list, stack)


    #To determine if the graph is bipartite - no 2 adjacent vertices have direct connection - using BFS
    #None --> bool (T if bipartite, F if not bipartite)
    def bicolor(self):
        visitedlist = []
        A = []
        B = []
        my_queue = QueueArray(100)
        bipartite = True
        while bipartite:
          for v in self.vertlist:
            if v.id not in visitedlist:
               visitedlist.append(v.id)
               A.append(v.id)
               for i in v.getConnection():
                   if i not in visitedlist:
                      visitedlist.append(i)
                      B.append(i)
                   vrtx = self.find_vertex(i, self.vertlist)
                   my_queue.enqueue(vrtx)
               bipartite = self.bfs(my_queue, B)
          break
        
        if bipartite == True:
           return True
        else:
           return False
 

    #Helper function to perform bfs
    #queue, list(B) --> bool
    def bfs(self, queue, list2):
        while queue.is_empty() is False:
           tmp = queue.dequeue()
           for i in tmp.getConnection():
               if i in list2:
                  return False       
        return True



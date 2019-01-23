#Project 4 - Hash Table Quadratic Probing
#Name: Ajay Patel
#Instructor: S. Einakian
#Section: 11


class HashTableQuadPr:

   #To create a hash table with a designated size
   #int(size) --> None
   def __init__(self, size = 251):
       self.table_size = size
       self.hash_table = [None] * self.table_size
       self.words = []


   #To read words from stop word file and place them in a hash table
   #file --> None
   def read_stop(self, filename):
       file = open(filename, 'r')
       line = file.readline()
       linecount = 0
       while line:
          dash = False
          for i in range(len(line) - 1):
              line = line.rstrip()
          for letter in line:
              if ord(letter) in range(33,45):
                 index = line.index(letter)
                 first = line[:index]
                 second = line[index + 1:]
                 line = first + second

              elif ord(letter) == 45:
                 index = line.index(letter)
                 first = line[:index]
                 second = line[index + 1:]
                 dash = True

              elif ord(letter) in range(46,65):
                 index = line.index(letter)
                 first = line[:index]
                 second = line[index + 1:]
                 line = first + second

              elif ord(letter) in range(91,97):
                 index = line.index(letter)
                 first = line[:index]
                 second = line[index + 1:]
                 line = first + second

              elif ord(letter) in range(123,127):
                 index = line.index(letter)
                 first = line[:index]
                 second = line[index + 1:]
                 line = first + second

          if dash == True:
             self.words.append(first)
             self.words.append(second)
          else:
             self.words.append(line)
             linecount += 1
 
          if len(self.words)/self.table_size >= .75:
             self.table_size = self.table_size * 2 + 1
             temp_table = [None] * self.table_size
             for i in self.words:
                 hash_value = self.myhash(i, self.table_size)
                 n = 0 
                 while temp_table[hash_value] != None:
                    n += 1
                    if (hash_value + (n**2)) > self.table_size:
                       hash_value = (hash_value + (n**2)) % self.table_size
                    else:              
                       hash_value = hash_value + (n**2) 

                 temp_table[hash_value] = i

             self.hash_table = temp_table

          else:
             hash_value = self.myhash(line, self.table_size)
             n = 0
             while self.hash_table[hash_value] != None:
                n += 1
                if (hash_value + (n**2)) > self.table_size - 1:
                   hash_value = (hash_value + (n**2)) % self.table_size
                else:
                   hash_value = hash_value + (n**2)
  
             self.hash_table[hash_value] = line

          line = file.readline()
       file.close()
       

   #To read words in the input file and insert into hash table 
   #filename, stop_table --> None
   def read_file(self, filename, stop_table):
       file = open(filename, 'r')
       line_number = 0
       for line in file:
           line = line.split()
           line_number += 1
           for word in line:
             if word.isdigit() == True:
                pass
             else:
               dash = False
               word = word.lower()
               for letter in word:
                   if ord(letter) in range(33,45):
                      index = word.index(letter)
                      first = word[:index]
                      second = word[index + 1:]
                      word = first + second

                   elif ord(letter) == 45:
                      index = word.index(letter)
                      first = word[:index] 
                      second = word[index + 1:]
                      dash = True
 
                   elif ord(letter) in range(46,65):
                      index = word.index(letter)
                      first = word[:index]
                      second = word[index + 1:]
                      word = first + second

                   elif ord(letter) in range(91,97):
                      index = word.index(letter)
                      first = word[:index]
                      second = word[index + 1:]
                      word = first + second

                   elif ord(letter) in range(123,127):
                      index = word.index(letter)
                      first = word[:index]
                      second = word[index + 1:]
                      word = first + second


               if dash == True:
                  if first in stop_table.hash_table:
                     pass
                  else:
                     self.words.append(first)
                     if self.get_load_fact() >= .75:
                        temp_size = self.table_size
                        self.table_size = self.table_size * 2 + 1
                        temp_hash_table = [None] * self.table_size
                        for i in self.words:
                            hash_value = self.myhash(i, temp_size)
                            index = hash_value
                            n = 1
                            while self.hash_table[index] != i:
                               index = hash_value + (n**2)
                               n += 1
                            item = self.hash_table[index]
                            new_index = self.myhash(item[0], self.table_size)
                            insert_index = new_index
                            n = 1
                            while temp_hash_table[insert_index] != None:
                               insert_index = new_index + (n**2)
                               n += 1
                            temp_hash_table[insert_index] = item

                        self.hash_table = temp_hash_table

                     else:
                        hash_value = self.myhash(first, self.table_size)
                        index = hash_value
                        repeat = False
                        n = 1
                        while self.hash_table[index] != None and not repeat:
                           if self.hash_table[index][0] == first:
                              list_of_lines = self.hash_table[index][1]
                              if list_of_lines[len(list_of_lines) - 1] != line_number:
                                 self.hash_table[index][1].append(line_number)
                              repeat = True
                           else:
                              index = hash_value + (n**2)
                              n += 1

                        if not repeat:
                           self.hash_table[index] = (first, [line_number])
            
                  if second in stop_table.hash_table:
                     pass
                  else:
                     self.words.append(second)
                     if self.get_load_fact() >= .75:
                        temp_size = self.table_size
                        self.table_size = self.table_size * 2 + 1
                        temp_hash_table = [None] * self.table_size
                        for i in self.words:
                            hash_value = self.myhash(i, temp_size)
                            index = hash_value
                            n = 1
                            while self.hash_table[index] != i:
                               index = hash_value + (n**2)
                               n += 1
                            item = self.hash_table[index]
                            new_index = self.myhash(item[0], self.table_size)
                            insert_index = new_index
                            n = 1
                            while temp_hash_table[insert_index] != None:
                               insert_index = new_index + (n**2)
                               n += 1
                            temp_hash_table[insert_index] = item

                        self.hash_table = temp_hash_table

                     else:
                        hash_value = self.myhash(second, self.table_size)
                        index = hash_value
                        repeat = False
                        n = 1
                        while self.hash_table[index] != None and not repeat:
                           if self.hash_table[index][0] == second:
                              list_of_lines = self.hash_table[index][1]
                              if list_of_lines[len(list_of_lines) - 1] != line_number:
                                 self.hash_table[index][1].append(line_number)
                              repeat = True
                           else:
                              index = hash_value + (n**2)
                              n += 1

                        if not repeat:
                           self.hash_table[index] = (second, [line_number])

               else:
                if word in stop_table.hash_table:
                   pass
                else:
                  self.words.append(word)
                  if self.get_load_fact() >= .75:
                     temp_size = self.table_size
                     self.table_size = self.table_size * 2 + 1
                     temp_hash_table = [None] * self.table_size
                     for i in self.words:
                         hash_value = self.myhash(i, temp_size)
                         index = hash_value
                         n = 1
                         while self.hash_table[index] != i:
                            index = hash_value + (n**2)
                            n += 1 
                         item = self.hash_table[index]
                         new_index = self.myhash(item[0], self.table_size)
                         insert_index = new_index
                         n = 1
                         while temp_hash_table[insert_index] != None:
                            insert_index = new_index + (n**2)
                            n += 1
                         temp_hash_table[insert_index] = item

                     self.hash_table = temp_hash_table

                  else:
                     hash_value = self.myhash(word, self.table_size)
                     index = hash_value
                     repeat = False
                     n = 1
                     while self.hash_table[index] != None and not repeat:
                        if self.hash_table[index][0] == word:
                           list_of_lines = self.hash_table[index][1]
                           if list_of_lines[len(list_of_lines) - 1] != line_number:
                              self.hash_table[index][1].append(line_number) 
                           repeat = True
                        else:
                           index = hash_value + (n**2)
                           n += 1

                     if not repeat:
                        self.hash_table[index] = (word, [line_number])


   #To return the size of the hash table 
   #None --> int
   def get_tablesize(self):
       return self.table_size

   
   #To return the output of words and frequencies
   #output filename --> None
   def save_concordance(self, output_filename):
       output_list = []
       for item in self.hash_table:
           if item != None:
              output_list.append(item)

       file = open(output_filename, 'w')
       sorted_list = sorted(output_list)    
       for item in sorted_list:
           final_output = item[0] + ":" + '\t'
           for i in item[1]:
               final_output = final_output + str(i) + ' '
           file.write(final_output + '\n')
       file.close()


   #To return the load factor of the Hash Table
   #None --> int
   def get_load_fact(self):
       return (len(self.words) / self.table_size)


   #To return the hash value integer for the hash table
   #int(key), int(table size) --> int
   def myhash(self, key, table_size):
       n = min(len(key), 8)
       hash_value = 0 
       for index in range(n):
           hash_value = hash_value + ord(key[index]) * 31**(n-1-index)
       return int(hash_value % table_size)


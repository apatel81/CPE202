#CPE 202 - Lab 8
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian

class MyHashTable:

   #To create a hash table of size 11
   #int(size) --> None
   def __init__(self, size = 11):
       self.table_size = size
       self.num_of_pairs = 0
       self.num_of_collisions = 0
       self.hash_table = [[] for _ in range(11)]


   #To insert an item into the Hash Table based on hash value. Need to consider
   #load factor and rehasing
   #key, item --> None
   def insert(self, key, item):
       if self.load_factor() >= 0.75:
          self.table_size = self.table_size * 2 + 1
          temp_hash_table = [[] for _ in range(self.table_size)]
          for section in self.hash_table:
              for pair in section:
                  hash_value = pair[0] % self.table_size
                  temp_hash_table[hash_value].append((pair[0], pair[1]))

          self.hash_table = temp_hash_table
          hash_value = key % self.table_size
          for pair in self.hash_table[hash_value]:
              if len(self.hash_table[hash_value]) != 0:
                 self.num_of_collisions += 1
                 if pair[0] == key:
                    self.hash_table[hash_value].remove(pair)
                    self.num_of_pairs -= 1
          self.hash_table[hash_value].append((key,item))
          self.num_of_pairs += 1
 
       else:
          hash_value = key % self.table_size
          for pair in self.hash_table[hash_value]:
              if len(self.hash_table[hash_value]) != 0:
                 self.num_of_collisions += 1
                 if pair[0] == key:
                    self.hash_table[hash_value].remove(pair)
                    self.num_of_pairs -= 1                 

          self.hash_table[hash_value].append((key, item))
          self.num_of_pairs += 1


   #To return the item in the hash table using its key 
   #int(key) --> item
   def get(self, key):
          hash_value = key % self.table_size
          for pair in self.hash_table[hash_value]:
              if pair[0] == key:
                 return pair[1]
          raise LookupError('Item not found')


   #To remove the item in the hash table using its key
   #int(key) --> key, item 
   def remove(self, key):
          hash_value = key % self.table_size
          for pair in self.hash_table[hash_value]:
              if pair[0] == key:
                 temp = pair
                 self.hash_table[hash_value].remove(pair)
                 self.num_of_pairs -= 1
                 return temp
          raise LookupError('Item not found')


   #To return the number of key-item pairs in the hash table
   #None --> int
   def size(self):
       return self.num_of_pairs


   #To return the current load factor of the hash table
   #None --> float
   def load_factor(self):
       return self.num_of_pairs/self.table_size


   #To return the number of collisions that have occurred in the hash table 
   #None --> int
   def collisions(self):
       return self.num_of_collisions

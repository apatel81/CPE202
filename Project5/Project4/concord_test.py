from hash_lin_table import *
import filecmp

# Create stop words hash table
stop_words = HashTableLinPr(251)            # start with table size of 251, grow as needed
stop_words.read_stop('stop_words.txt')      # read in stop words, load hash table

# Create concordance hash table
concord = HashTableLinPr(251)               # start with table size of 251, grow as needed
concord.read_file('input1.txt',stop_words)  # read from file, process as required, load hash table
concord.save_concordance('test1.txt')       # save (write) concordance to file

# Compare test1.txt file to known good concord1.txt file
print("File compare:", filecmp.cmp('test1.txt','input1_sol.txt')) # will be True if files match# 
#Create concordance hash table
concord = HashTableLinPr(251)               # start with table size of 251, grow as needed
concord.read_file('input2.txt',stop_words)  # read from file, process as required, load hash table
concord.save_concordance('test2.txt')       # save (write) concordance to file

# Compare test1.txt file to known good concord1.txt file
print("File compare:", filecmp.cmp('test2.txt','input2_sol.txt')) # will be True if files match

from hash_quad_table import *

# Create stop words hash table
stop_words = HashTableQuadPr(251)            # start with table size of 251, grow as needed
stop_words.read_stop('stop_words.txt')      # read in stop words, load hash table

# Create concordance hash table
concord = HashTableQuadPr(251)               # start with table size of 251, grow as needed
concord.read_file('input1.txt',stop_words)  # read from file, process as required, load hash table
concord.save_concordance('qtest1.txt')       # save (write) concordance to file

# Compare test1.txt file to known good concord1.txt file
print("File compare:", filecmp.cmp('qtest1.txt','input1_sol.txt')) # will be True if files match# 
#Create concordance hash table
concord = HashTableQuadPr(251)               # start with table size of 251, grow as needed
concord.read_file('input2.txt',stop_words)  # read from file, process as required, load hash table
concord.save_concordance('qtest2.txt')       # save (write) concordance to file

# Compare test1.txt file to known good concord1.txt file
print("File compare:", filecmp.cmp('qtest2.txt','input2_sol.txt')) # will be True if files match

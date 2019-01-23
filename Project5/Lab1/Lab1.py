#CPE 202 - Lab 1
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian

def find_max(list):
    #iterate through the list to find the max value
    #list --> integer or float
    if len(list) == 0:
       raise ValueError('Empty List')
    elif len(list) == 1:
       return list[0]
    else: 
       x = list[0]
       for items in list:
           if items > x:
              x = items
       return x


def rev_string(string):
    #recursive function that takes string and returns string backwards
    #str --> str(backwards)
    if string == "":
       return string
    else:
       return string[-1] + rev_string(string[:-1])


def bin_search(target, low, high, list_val):
    #recursive function that searches list of ints
    #list ---> index of target
    list_val.sort()
    midpoint = (low + high)//2
    if len(list_val) == 0:
       return None
    if target not in list_val:
       return None
    if list_val[midpoint] == target:
       return midpoint
    elif target < list_val[midpoint]:
       return bin_search(target, low, midpoint - 1, list_val)
    elif target > list_val[midpoint]:
       return bin_search(target, midpoint + 1, high, list_val)
           

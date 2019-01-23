#CPE 202 - Lab 6
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian


import time
import random 
import copy


#To sort an unsorted list by taking items one by one from the unsorted and placing them in sorted list
#list --> list
def insertion_sort(lst1):
    start_time = time.time()
    lst2 = copy.copy(lst1)
    size = len(lst2)
    count = 0
    for index in range(1, size):
        current_value = lst2[index]
        position = index
        while position > 0 and lst2[position - 1] > current_value:
              lst2[position] = lst2[position - 1]
              count += 1
              position -= 1
        lst2[position] = current_value
    end_time = time.time()
    sort_time = end_time - start_time
    #return sort_time, count
    return lst2

#To sort an unsorted list by comparing the indexes in order and assigning min index
#list --> list
def selection_sort(alist):
    start_time = time.time()
    count = 0
    for i in range(len(alist)):
        minidx = i
        for k in range(i + 1, len(alist)):
            if alist[k] < alist[minidx]:
               count += 1
               minidx = k 
        swap(alist, minidx, i)
    end_time = time.time()
    sort_time = end_time - start_time
    #return sort_time, count
    return alist

#To swap items in the list in selection sort
#list, int(index), int(i)  --> None
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp


#To split list in half, sort each segment, and then merge 2 together
#list -->
def merge_sort(alist):
    start_time = time.time()
    count = 0
    if len(alist) > 1:
       count += 1
       mid = len(alist)//2
       left = alist[:mid]
       right = alist[mid:]
       
       merge_sort(left)
       merge_sort(right)

       i = 0
       j = 0
       k = 0

       while i < len(left) and j < len(right):
          if left[i] < right[j]:
             count += 1
             alist[k] = left[i]
             i += 1
          else:
             count += 1
             alist[k] = right[j]
             j += 1
          k += 1

       while i < len(left):
          count += 1
          alist[k] = left[i]
          i += 1
          k += 1

       while j < len(right):
          count += 1
          alist[k] = right[j]
          j += 1
          k += 1
    end_time = time.time()
    sort_time = end_time - start_time
    #return sort_time, count
    return alist


#To sort this list using a pointer and then comparing/rearrange values based on the pointer
#list --> list
def _partition(mylist, start, end):
    count = 0
    pos = start
    for i in range(start, end):
        count += 1
        if mylist[i] < mylist[end]:
            mylist[i], mylist[pos] = mylist[pos], mylist[i]
            pos += 1
    mylist[pos], mylist[end] = mylist[end], mylist[pos]
    return pos, count

def _quicksort(mylist, start, end):
    count = 0
    if start < end:
        pos, count = _partition(mylist, start, end)        
        count += _quicksort(mylist, start, pos - 1)
        count += _quicksort(mylist, pos + 1, end)
    return count

def quick_sort(mylist, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(mylist) - 1
    return _quicksort(mylist, start, end)

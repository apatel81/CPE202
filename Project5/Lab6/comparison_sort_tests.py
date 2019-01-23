#CPE 202 - Lab 6 Test Cases
#Name: Ajay Patel
#Section: 11
#Instructor: S. Einakian


import random
import unittest
import sys
from comparison_sort import *




#print(sys.getrecursionlimit())
#sys.setrecursionlimit(1000000)



class test_expressions(unittest.TestCase):

      def test_seleciton_sort(self):
          alist = random.sample(range(10000), 10)
          blist = [5445, 8692, 6915, 8637, 4848, 9408, 1744, 171, 4315, 2949]
          self.assertEqual(selection_sort(blist), [171, 1744, 2949, 4315, 4848, 5445, 6915, 8637, 8692, 9408])

      def test_insertion_sort(self): 
          blist = [5445, 8692, 6915, 8637, 4848, 9408, 1744, 171, 4315, 2949]
          self.assertEqual(insertion_sort(blist), [171, 1744, 2949, 4315, 4848, 5445, 6915, 8637, 8692, 9408])


      def test_merge_sort(self):
          blist = [5445, 8692, 6915, 8637, 4848, 9408, 1744, 171, 4315, 2949]
          self.assertEqual(merge_sort(blist), [171, 1744, 2949, 4315, 4848, 5445, 6915, 8637, 8692, 9408])
 
      def test_quick_sort(self):
          blist = [5445, 8692, 6915, 8637, 4848, 9408, 1744, 171, 4315, 2949]
          self.assertEqual(quick_sort(blist), 22) #[171, 1744, 2949, 4315, 4848, 5445, 6915, 8637, 8692, 9408])




if __name__ == "__main__":
    unittest.main()




#UNSORTED

"""list1 = random.sample(range(10000), 1000)
print("Insertion Sort, 1000: ", insertion_sort(list1))
print("Selection Sort, 1000: ", selection_sort(list1))
print("Merge Sort, 1000: ", merge_sort(list1))
start_time = time.time()
print("Quick Sort, 1000: ", quick_sort(list1))
end_time = time.time()
print(end_time - start_time)

print("")

list2 = random.sample(range(10000), 2000)
print("Insertion Sort, 2000: ", insertion_sort(list2))
print("Selection Sort, 2000: ", selection_sort(list2))
print("Merge Sort, 2000: ", merge_sort(list2))
start_time = time.time()
print("Quick Sort, 2000: ", quick_sort(list2))
end_time = time.time()
print(end_time - start_time)

print("")

list3 = random.sample(range(10000), 3000)
print("Insertion Sort, 3000: ", insertion_sort(list3))
print("Selection Sort, 3000: ", selection_sort(list3))
print("Merge Sort, 3000: ", merge_sort(list3))
start_time = time.time()
print("Quick Sort, 3000: ", quick_sort(list3))
end_time = time.time()
print(end_time - start_time)

print("")

list4 = random.sample(range(10000), 4000)
print("Insertion Sort, 4000: ", insertion_sort(list4))
print("Selection Sort, 4000: ", selection_sort(list4))
print("Merge Sort, 4000: ", merge_sort(list4))
start_time = time.time()
print("Quick Sort, 4000: ", quick_sort(list4))
end_time = time.time()
print(end_time - start_time)

print("")

list5 = random.sample(range(10000), 8000)
print("Insertion Sort, 8000: ", insertion_sort(list5))
print("Selection Sort, 8000: ", selection_sort(list5))
print("Merge Sort, 8000: ", merge_sort(list5))
start_time = time.time()
print("Quick Sort, 8000: ", quick_sort(list5))
end_time = time.time()
print(end_time - start_time)

print("")

list6 = random.sample(range(20000), 16000)
print("Insertion Sort, 16000: ", insertion_sort(list6))
print("Selection Sort, 16000: ", selection_sort(list6))
print("Merge Sort, 16000: ", merge_sort(list6))
start_time = time.time()
print("Quick Sort, 16000: ", quick_sort(list6))
end_time = time.time()
print(end_time - start_time)

print("")

list7 = random.sample(range(40000), 32000)
print("Insertion Sort, 32000: ", insertion_sort(list7))
print("Selection Sort, 32000: ", selection_sort(list7))
print("Merge Sort, 32000: ", merge_sort(list7))
start_time = time.time()
print("Quick Sort, 32000: ", quick_sort(list7))
end_time = time.time()
print(end_time - start_time)

print("")

list8 = random.sample(range(200000), 100000)
print("Insertion Sort, 100000: ", insertion_sort(list8))
print("Selection Sort, 100000: ", selection_sort(list8))
print("Merge Sort, 100000: ", merge_sort(list8))
start_time = time.time()
print("Quick Sort, 100000: ", quick_sort(list8))
end_time = time.time()
print(end_time - start_time)

print("")

list9 = random.sample(range(1000000), 500000)
print("Insertion Sort, 500000: ", insertion_sort(list9))
print("Selection Sort, 500000: ", selection_sort(list9))
print("Merge Sort, 500000: ", merge_sort(list9))
start_time = time.time()
print("Quick Sort, 500000: ", quick_sort(list9))
end_time = time.time()
print(end_time - start_time)

print("")


#SORTED
        
list1 = random.sample(range(10000), 1000)
list1.sort()
print("Insertion Sort, 1000: ", insertion_sort(list1))
print("Selection Sort, 1000: ", selection_sort(list1))
print("Merge Sort, 1000: ", merge_sort(list1))
start_time = time.time()
print("Quick Sort, 1000: ", quick_sort(list1))
end_time = time.time()
print(end_time - start_time)

print("")

list2 = random.sample(range(10000), 2000)
list2.sort()
print("Insertion Sort, 2000: ", insertion_sort(list2))
print("Selection Sort, 2000: ", selection_sort(list2))
print("Merge Sort, 2000: ", merge_sort(list2))
start_time = time.time()
print("Quick Sort, 2000: ", quick_sort(list2))
end_time = time.time()
print(end_time - start_time)

print("")

list3 = random.sample(range(10000), 3000)
list3.sort()
print("Insertion Sort, 3000: ", insertion_sort(list3))
print("Selection Sort, 3000: ", selection_sort(list3))
print("Merge Sort, 3000: ", merge_sort(list3))
start_time = time.time()
print("Quick Sort, 3000: ", quick_sort(list3))
end_time = time.time()
print(end_time - start_time)

print("")

list4 = random.sample(range(10000), 4000)
list4.sort()
print("Insertion Sort, 4000: ", insertion_sort(list4))
print("Selection Sort, 4000: ", selection_sort(list4))
print("Merge Sort, 4000: ", merge_sort(list4))
start_time = time.time()
print("Quick Sort, 4000: ", quick_sort(list4))
end_time = time.time()
print(end_time - start_time)

print("")

list5 = random.sample(range(10000), 8000)
list5.sort()
print("Insertion Sort, 8000: ", insertion_sort(list5))
print("Selection Sort, 8000: ", selection_sort(list5))
print("Merge Sort, 8000: ", merge_sort(list5))
print("Quick Sort, 8000: ", quick_sort(list5))

print("")

list6 = random.sample(range(20000), 16000)
list6.sort()
print("Insertion Sort, 16000: ", insertion_sort(list6))
print("Selection Sort, 16000: ", selection_sort(list6))
print("Merge Sort, 16000: ", merge_sort(list6))
start_time = time.time()
print("Quick Sort, 16000: ", quick_sort(list6))
end_time = time.time()
print(end_time - start_time)

print("")

list7 = random.sample(range(40000), 32000)
list7.sort()
print("Insertion Sort, 32000: ", insertion_sort(list7))
print("Selection Sort, 32000: ", selection_sort(list7))
print("Merge Sort, 32000: ", merge_sort(list7))
start_time = time.time()
print("Quick Sort, 32000: ", quick_sort(list7))
end_time = time.time()
print(end_time - start_time)

print("")

list8 = random.sample(range(200000), 100000)
list8.sort()
print("Insertion Sort, 100000: ", insertion_sort(list8))
print("Selection Sort, 100000: ", selection_sort(list8))
print("Merge Sort, 100000: ", merge_sort(list8))
start_time = time.time()
print("Quick Sort, 100000: ", quick_sort(list8))
end_time = time.time()
print(end_time - start_time)

print("")

list9 = random.sample(range(1000000), 500000)
list9.sort()
print("Insertion Sort, 500000: ", insertion_sort(list9))
print("Selection Sort, 500000: ", selection_sort(list9))
print("Merge Sort, 500000: ", merge_sort(list9))
start_time = time.time()
print("Quick Sort, 500000: ", quick_sort(list9))
end_time = time.time()
print(end_time - start_time)"""

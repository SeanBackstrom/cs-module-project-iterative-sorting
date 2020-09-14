# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    if not arr:
        return arr
    _sorted = []
    _unsorted = arr

    arr_len = len(arr)

    for j in range(0, arr_len):
        current_min = _unsorted[0]
        #find min
        for i in range(0, len(_unsorted)):
            
            if _unsorted[i] < current_min:
                current_min = _unsorted[i]
            

        #append found min
        _sorted.append(current_min)
        _unsorted.remove(current_min)
    arr = _sorted
    return arr

import random
arr4 = random.sample(range(200), 50)


print(selection_sort(arr4))
print(len(selection_sort(arr4)))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    if not arr:
        return arr

    total_arr = len(arr) - 1
    total_sorted = 0

    while total_sorted != total_arr:
        for num in range(total_arr):
            comp_arr = [arr[num], arr[num+1]]
            left = comp_arr[0]
            right = comp_arr[1]

            if right < left:
                placehold_left = left
                left = right
                right = placehold_left
                arr[num] = left
                arr[num+1] = right
            else:
                pass
        #check if all is sorted
        total_sorted = 0
        for i in range(total_arr):   
            
 
            comp_arr = [arr[i], arr[i+1]]
            left = comp_arr[0]
            right = comp_arr[1]      
            if right > left:
                total_sorted +=1

    return arr


    
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr

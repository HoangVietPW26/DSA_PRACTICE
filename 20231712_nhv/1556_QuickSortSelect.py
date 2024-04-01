

#partitioning
"""
To partition an array is to take a random value from the array—which is then
called the pivot—and make sure that every number that is less than the pivot
ends up to the left of the pivot, and that every number greater than the pivot
ends up to the right of the pivot.
- pivot will always stay at the right place after partition

0,5,2,1,6,3

Select 3 as PIVOT
We then assign “pointers”—one to the left-most value of the array, and one
to the rightmost value of the array, excluding the pivot itself:

0*,5,2,1,6*,(3)
1. The left pointer continuously moves one cell to the right until it reaches
a value that is greater than or equal to the pivot, and then stops
0, 5*,2,1,6, (3) - 5>3 -> stop


2. the right pointer continuously moves one cell to the left until it
reaches a value that is less than or equal to the pivot, and then stops.
The right pointer will also stop if it reaches the beginning of the array.
0,5*,2,1*,6,(3) - 1<3 -> stop

3. Once the right pointer has stopped, we reach a crossroads. If the left
pointer has reached (or gone beyond) the right pointer, we move on to
Step 4. Otherwise, we swap the values that the left and right pointers are
pointing to, and then go back to repeat Steps 1, 2, and 3 again.

0,1*,2,5*,6,(3)

Repeat left ponit:
0,1,2*,5*,6,(3) 2<3 -> continue
0,1,2,5**,6,(3) 5>3 -> stop

Repeat right ponit:
0,1,2,5**,6,(3) 5>3 -> stop
left reach/beyond right -> step 4

4. Finally, we swap the pivot with the value that the left pointer is currently
pointing to.
0,1,2,3,6,5
-> not sorted but complete one partition
"""
def partition(arr, left_pointer, right_pointer): #O(N)
    # We always choose the right-most element as the pivot.
    # We keep the index of the pivot for later use:
    pivot_index = right_pointer
    # We grab the pivot value itself:
    pivot = arr[pivot_index]
    # We start the right pointer immediately to the left of the pivot
    right_pointer -= 1
    while True:
    # Move the left pointer to the right as long as it
    # points to value that is less than the pivot:
        while arr[left_pointer] < pivot:
            left_pointer += 1
    # Move the right pointer to the left as long as it
    # points to a value that is greater than the pivot:
        while arr[right_pointer] > pivot:
            right_pointer -= 1
    # We've now reached the point where we've stopped
    # moving both the left and right pointers.
    # We check whether the left pointer has reached
    # or gone beyond the right pointer. If it has,
    # we break out of the loop so we can swap the pivot later
    # on in our code:
        if left_pointer >= right_pointer:
            break
    # If the left pointer is still to the left of the right
    # pointer, we swap the values of the left and right pointers:
        else:
            arr[left_pointer], arr[right_pointer] =  \
            arr[right_pointer], arr[left_pointer]
    # We move the left pointer over to the right, gearing up
    # for the next round of left and right pointer movements:
            left_pointer += 1

    # of the left pointer with the pivot:
    arr[left_pointer], arr[pivot_index] = \
    arr[pivot_index], arr[left_pointer]
    # We return the left_pointer for the sake of the quicksort method
    # which will appear later in this chapter:
    return left_pointer

"""
The Quicksort algorithm is a combination of partitions and recursion. It works
as follows:
1. Partition the array. The pivot is now in its proper place.
2. Treat the subarrays to the left and right of the pivot as their own arrays,
and recursively repeat Steps 1 and 2. That means we’ll partition each
subarray and end up with even smaller sub-subarrays to the left and
right of each subarray’s pivot. We then partition those sub-subarrays,
and so on and so forth.
3. When we have a subarray that has zero or one elements, that is our base
case and we do nothing.

0,1,2,3,6,5 (3) is original pivot
now partition 0*,1*,2 (2):
- 0 < 2 -> continue
0,1**,2:
- 1<2 -> continue:
0,1*,2*:
- 2=2 -> stop left
0,1*,2*:
- 1<2: stop right
left > right -> swap with pivot: 0,1,2 (2) is pivot now
now partition: 0**,1, (1):
- 0 < 1: continue
0*,1*:
- 1=1: stop left
- 0<1: stop right, left > right -> swap with pivot -> 0,1 (1) is pivot now
- 0 is subarray -> stop

now partition 6**,5 (5):
- 6 > 5 -> stop left
- 5 < 6 -> stop right, left = right: swap left with pivot:
5,6**
6 is subarray -> stop
"""
def quicksort(arr, left_index, right_index): 
# Base case: the subarray has 0 or 1 elements:
    if right_index - left_index <= 0:
        return arr
    # Partition the range of elements and grab the index of the pivot:
    pivot_index = partition(arr, left_index, right_index)
    # Recursively call this quicksort! method on whatever
    # is to the left of the pivot:
    quicksort(arr, left_index, pivot_index - 1)
    # Recursively call this quicksort! method on whatever
    # is to the right of the pivot:
    quicksort(arr, pivot_index + 1, right_index)
    # actually this will cause error since the outside quicksort not return

"""
            Best        Avg         Worst
Insertion   O(N)        O(N^2)      O(N^2)
Qucik       O(NlogN)    O(NlogN)    O(N^2)
"""

#QuickSelect
"""
Find k-lowest/hight value in the array
Ex: Fifth highest, array of len 8

1. Partition: pivot somewhere at the middle ex: 5th
    if pivot at 5th -> number is pivot itself
Now look for second highest -> it must be on the left of pivot
2. partition the left side of array, pivot end up at 3rd
    -> second highest is on the left of pivot
3. partition the left side: pivot at 2nd -> grab the value
8 len -> 3 partitionmaximun 8+4+2 = 16 = 2*8 step
Quick select is O(2N) -> O(N)

"""

def quick_select(arr, k_lowest_value, left_index, right_index):
    if right_index - left_index <= 0:
        return arr[left_index]
    
    pivot_index = partition(left_index, right_index) #O(N)
    if k_lowest_value < pivot_index:
        quick_select(arr, k_lowest_value, left_index, pivot_index - 1)
    elif k_lowest_value > pivot_index:
        quick_select(arr, k_lowest_value, pivot_index + 1, right_index)
    else:
        return arr[pivot_index]
    
"""
QuickSelect has O(N) for avg case, O(N^2) for worst case
"""

"""
Given an array of positive numbers, write a function that returns the
greatest product of any three numbers. The approach of using three
nested loops would clock in at O(N3), which is very slow. Use sorting to
implement the function in a way that it computes at O(N log N) speed.
(There are even faster implementations, but we’re focusing on using
sorting as a technique to make code faster.)
"""
def three_greates_product(arr: list) -> int:
    def partition(arr, left_index, right_index):
        pivot_index = right_index
        pivot = arr[pivot_index]
        right_index -= 1
        while True:
            while arr[left_index] < pivot:
                left_index += 1
            while arr[right_index] > pivot:
                right_index -= 1
            
            if left_index >= right_index:
                break
            else:
                arr[left_index], arr[right_index] = \
                arr[right_index], arr[left_index]
                left_index += 1
        
        arr[left_index], arr[pivot_index] =\
        arr[pivot_index], arr[left_index]

        return left_index
    
    def quick_sort(arr, left_index, right_index):
        if left_index < right_index:

            pivot_index = partition(arr, left_index, right_index)

            quick_sort(arr, left_index, pivot_index - 1)
            quick_sort(arr, pivot_index + 1, right_index)

        return arr



    arr = quick_sort(arr, 0, len(arr)-1)
    return arr[-1]*arr[-2]*arr[-3]

"""
The following function finds the “missing number” from an array of integers. That is, the array is expected to have all integers from 0 up to the array’s length, but one is missing. As examples, the array, [5, 2, 4, 1, 0] is missing the number 3, and the array, [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the number 8.
Here’s an implementation that is O(N2) (the includes method alone is already O(N), since the computer needs to search the entire array to find n):
function findMissingNumber(array) {
    for(let i = 0; i < array.length; i++) {
        if(!array.includes(i)) {
            return i;
        }
    }
    // If all numbers are present:
    return null;
}
Use sorting to write a new implementation of this function that only takes
O(N log N). (There are even faster implementations, but we’re focusing on
using sorting as a technique to make code faster.)
"""
def missing_value(arr: list) -> int:
    def partition(arr, left_index, right_index):
        pivot_index = right_index
        pivot = arr[pivot_index]
        right_index -= 1
        while True:
            while arr[left_index] < pivot:
                left_index += 1
            while arr[right_index] > pivot:
                right_index -= 1
            
            if left_index >= right_index:
                break
            else:
                arr[left_index], arr[right_index] = \
                arr[right_index], arr[left_index]
                left_index += 1
        
        arr[left_index], arr[pivot_index] =\
        arr[pivot_index], arr[left_index]

        return left_index
    
    def quick_sort(arr, left_index, right_index):
        if left_index < right_index:

            pivot_index = partition(arr, left_index, right_index)

            quick_sort(arr, left_index, pivot_index - 1)
            quick_sort(arr, pivot_index + 1, right_index)

        return arr
    
    arr = quick_sort(arr, 0, len(arr)-1)
    for i in range(len(arr)):
        if arr[i] != i:
            return i
    return 0

"""
Write three different implementations of a function that finds the greatest
number within an array. Write one function that is O(N2), one that is O(N
log N), and one that is O(N).

"""

if __name__ == "__main__":
    print(three_greates_product([2,3,4,9,9,5]))
    print(missing_value([1,2,3,4,5]))



        
        
            

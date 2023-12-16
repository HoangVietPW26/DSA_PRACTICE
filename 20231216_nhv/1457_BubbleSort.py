#Speeding up your code common to DSA chapter 4

"""
Bubble Sort is a basic sorting algorithm and follows these steps:
1. Point to two consecutive values in the array. 
(Initially, we start by pointing to the array’s first two values.) 
Compare the first item with the second one:
- 2,1,3,5 (2 and 1)

2. If the two items are out of order 
(in other words, the left value is greater  than the right value), 
swap them (if they already happen to be in the correct order, 
do nothing for this step):
- 1,2,3,5

3. Move the “pointers” one cell to the right:
- 1,2,3,5 (2 and 3)

4. Repeat Steps 1 through 3 until we reach the end of the array, 
or if we reach the values that have already been sorted 
(value already in the rightmost place of it in actual)
Note that the highest unsorted element will always move to the 
rightmost at the end of pass through
At this point, we have completed our first pass-through of the array. 
That is, we “passed through” the array by pointing to each of 
its values until we reached the end.

5. We then move the two pointers back to the first two values of the array,
and execute another pass-through of the array by running Steps 1 through
4 again. We keep on executing these pass-throughs until we have a passthrough 
in which we did not perform any swaps. 
When this happens, it means our array is fully sorted and our work is done.
"""

# implement bubble sorted  

def bubble_sort(lst: list) -> list:
    unsorted_until_index = len(lst) - 1 # rightmost index that has nt yet been sorted
    is_sorted = False # flag to make sure lst is sorted
    while not is_sorted:
        is_sorted = True
        for i in range(unsorted_until_index):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
            is_sorted = False
        unsorted_until_index -= 1
    return lst

# Efficiency
"""
If length of list is 5, and it is in desxending order
-> for each pass through, we need 4N - (1+2+3+4) comparison steps,
eaxh step need 1 swap -> total 2*(4N-(1+2+3+4)) steps
If lenght is N, we need 2*(N-1)N - (1+2+...+(N-1)) -> O(N^2) -> quadaratic times
"""

# from O(N^2) to O(N)

"""
For example, the array [1, 5, 3, 9, 1, 4] 
has two instances of the number 1,
so we’d return true to indicate that the array has a 
case of duplicate numbers.
"""
lst = [1, 5, 3, 9 ,5 ,4] 
#Brute-force
# 1. loop through each elements, element i
# 2. loop through each element in a nested loop, element j
# 3. If they are the same, return true
def hasDuplicateValueBF(lst: list) -> bool:
    step = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            step += 1
            if lst[i] == lst[j] and i != j:
                print(f"Total step is {step}")
                return True
    print(f"Total step is {step}")
    return False

# O(N^2)

# Imprvement
"""
1. create existing number list, the list contain arbitary value 1, 
at the index refer to the value in the list
Ex: [3,5,6]
exist = [null, null, null, 1, null, 1, 1]
2. If the lst has duplicated value -> 
exist will already have 1 in the refer indedx -> True
We need to loop only once -> O(N)
JS solution, this will cause list index out of rage in python

function hasDuplicateValue(array) {
    let existingNumbers = [];
    for(let i = 0; i < array.length; i++) {
            if(existingNumbers[array[i]] === 1) {
                return true;
        } else {
            existingNumbers[array[i]] = 1;
        }
    }
    return false;
}

In python we use set
"""
def hasDuplicateValue(lst: list) -> bool:
    step = 0
    existingNumbers = set()
    for i in range(len(lst)):
        step += 1
        if lst[i] in existingNumbers:
            print(f"Total step is {step}")
            return True
        else:
            existingNumbers.add(lst[i]) # set add is O(1)
    print(f"Total step is {step}")
    return False

if __name__ == "__main__":
    print(hasDuplicateValueBF(lst))
    print(hasDuplicateValue(lst))

#Prob1: It finds the greatest product of any pair of two numbers within a
# given array:
def greatestProduct(array):
    greatestProductSoFar = array[0] * array[1]
    for i, iVal in enumerate(array):
        for j, jVal in enumerate(array):
            if i != j and iVal * jVal > greatestProductSoFar:
                greatestProductSoFar = iVal * jVal
    return greatestProductSoFar
# O(N^2)

#Prob2: the greatest single number within an array,
# but has an efficiency of O(N2). Rewrite the function so that it becomes a
# speedy O(N):
def greatestNumberBF(lst):
    for i in lst:
        # Assume for now that i is the greatest:
        isIValTheGreatest = True
        for j in lst:
        # If we find another value that is greater than i,
        # i is not the greatest:
            if j > i:
                isIValTheGreatest = False
    # If, by the time we checked all the other numbers, i
    # is still the greatest, it means that i is the greatest number:
    if isIValTheGreatest:
        return i
    
def greatestNumbers(lst: list) -> bool:
    #Edge case lst is nempty
    if len(lst) == 0:
        return
    # Assume gratest number is the first element
    greatest = lst[0]
    for i in lst:
        # if index i element is higher than greatest, greates become that ele
        if i > greatest:
            greatest = i
    return greatest
#O(N)

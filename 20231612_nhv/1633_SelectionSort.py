"""
1. We check each cell of the array from left to right to determine which value
is least and keep track of the lowaest value so far.
(We’ll do this by storing its index in a variable.)
If we encounter a cell that contains a value that is even lower than the
one in our variable, we replace it so that the variable now points to the
new index.
If not find the lower, we do nothing

- 2*,6,1,3: lowest is 2, index is 0
- 2,6*,1,3: lowest is 2, index is 0
- 2,6,1*,3: lowest is 1, index is 2
- 2,6,1,3*: lowest is 1, index is 2

2. Once we’ve determined which index contains the lowest value, 
we swap its value with the value we began the pass-through with. 
This would be index 0 in the first pass-through, index 1 in the 
second pass-through, and so on.
Note that the lowest will always stay at the most left ordered position 
after each pass through.
- 2,6,1,3 -> 1,6,2,3

3. Each pass-through consists of Steps 1 and 2.
We repeat the pass-throughs until we reach a pass-through that would
start at the end of the array. 
By this point, the array will have been fully sorted.
- 2,6,1**,3 -> 1,6,2**,3 -> 1,2,6,3** -> 1,2,3,6** (** is the smallest)

JS selection sort:
function selectionSort(array) {
    for(let i = 0; i < array.length - 1; i++) {
        let lowestNumberIndex = i;
        for(let j = i + 1; j < array.length; j++) {
            if(array[j] < array[lowestNumberIndex]) {
                lowestNumberIndex = j;
            }
        }
        if(lowestNumberIndex != i) {
            let temp = array[i];
            array[i] = array[lowestNumberIndex];
            array[lowestNumberIndex] = temp;
        }
    }
    return array;
}
"""
lst = [4,2,7,1,3]
#Implementation
def selection_sort(lst: list) -> list:
    for i in range(len(lst)):
        indexOfLowest = i
        lowest = lst[i]
        for j in range(i, len(lst)):
            if lst[j] < lowest:
                lowest = lst[j]
                indexOfLowest = j
        lst[i], lst[indexOfLowest] = lst[indexOfLowest], lst[i]
        print(lst)
    return lst
if __name__ == "__main__":
    print(selection_sort(lst))
"""
Selction Sort still have O(N^2) but twice faster tha bubble , actually O(N^2/2)
2 algo woth same big O, 1 may still faster
"""

def print_numbers_version_one(upperLimit):
    number = 2
    while number <= upperLimit:
        # If number is even, print it:
        if number % 2 == 0:
            print(number)
        number += 1
    # This takes N steps
def print_numbers_version_two(upperLimit):
    number = 2
    while number <= upperLimit:
        print(number)
        # Increase number by 2, which, by definition,
        # is the next even number:
        number += 2
    # This takes N/2 steps
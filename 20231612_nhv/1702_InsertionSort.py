# Common Guide To DSA chapter 6

"""
We need to consider not only the worst case

1. In the first pass-through, we temporarily remove the value at index 1 
(the second cell) and store it in a temporary variable. 
This will leave a gap at that index, since it contains no value:
- 8,4,2,3 -> 8, ,2,3 | [4]
In subsequent pass-throughs, we remove the values at the subsequent
indexes.

2. We then begin a shifting phase, where we take each value to the left of
the gap and compare it to the value in the temporary variable via 
position index - 1:
- 8*, ,2,3 | 8 (index 1-1) compare to 4

As we shift values to the right, inherently the gap moves leftward. 
As soon as we encounter a value that is lower than  the temporarily removed value,
or we reach the left end of the array, this shifting phase is over.

We then insert the temporarily removed value into the current gap:

- 4,8,2,3

3. Steps 1 through 3 represent a single pass-through. 
We repeat these passthroughs until the pass-through begins at the final 
index of the array. By then, the array will have been fully sorted.
- 4,8,2,3 -> 4,8, ,3 | temp = 2
- 8 > 2 (index 2-1) -> 4, ,8,3 -> 4>2 (index 2-2) ->  ,4,8,3 -> stop -> 2,4,8,3
- 2,4,8,3 -> 2,4,8, | temp = 3
- 8>3 (index 3-1) -> 2,4, ,8 -> 4>3 (index 3-2) -> 2, ,4,8 -> 2<3 (index 3-3) -> stop -> 2,3,4,8
"""

#implement
def insertion_sort(lst: list) -> list:
    for i in range(1, len(lst)):
        temp = lst[i]
        position = i - 1
        while position >= 0:
            if(lst[position]) > temp:
                lst[position+1] = lst[position] 
                position -= 1
            else:
                break
        lst[position+1] = temp
    return lst

if __name__ == "__main__":
    print(insertion_sort([4,2,7,1,3]))

"""
Selection: Best N^2/2, Avg: N^2/2, worst: N^2/2 
Insertion: Best N, Avg: N^2/2, worst: N^2
"""

"""
The following function returns whether or not a capital “X” is present
within a string.
What is this function’s time complexity in terms of Big O Notation?
Then, modify the code to improve the algorithm’s efficiency for best- and
average case
"""
def containsX(string: str):
    foundX = False
    for c in string:
        if c == "X":
            foundX = True
    return foundX
#O(N)
def containsX(string: str):
    for c in string:
        if c == "X":
            return True
    return False
# Best: O(1), Avg: O(N) N< string length, Worst: O(N)
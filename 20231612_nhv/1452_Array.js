```
The array is one of the most basic data structures in computer science.
array = ["apples", "bananas", "cucumbers", "dates", "elderberries"]
```

```
DSA Operation:
1, Read: looking something up at a particular spot within
the data structure. With an array, this means looking up a value at a
particular index

2, Search:  Searching refers to looking for a particular value within a data
structure. With an array, this means looking to see if a particular value
exists within the array, and if so, at which index

3,Insert: Insertion refers to adding a new value to our data structure. With
an array, this means adding a new value to an additional slot within the
array. 

4, Delete: Deletion refers to removing a value from our data structure. With
an array, this means removing one of the values from the array.
```

//Measure speed of operation
// Reading
```
A computer can read from an array in just one step bcuz:
1. When a program declares an array, it allocates a contiguous set of empty
cells for use in the program, every cell has specific address, computer also
make a note at which address array begin
2. A computer can jump to any memory address in one step.
3. By logical extension +,- if find the 2nd, 3rd indexs ...

For ex,
1. The array begins with index 0, which is at memory address 1010.
2. Index 3 will be exactly three slots past index 0.
3. By logical extension, index 3 would be located at memory address 1013,
since 1010 + 3 is 1013
```
// Searching
```
To search for a fruit within the array, the computer has no choice but to
inspect each cell one at a time. -> for N cell array it takse up to N times
```
//Insertion
```
This is true due to another fact about computers: when allocating an array,
the computer always keeps track of the array’s size.

If insert at the end item. 
Once the computer calculates which memory address to insert the new value
into, it can do so in one step.

If insert at beginning or middle, 
The comp need to shift pieces of data to make room for what we’re
inserting, leading to additional steps. Ex: 5 ele array and we insert to index no3,
We have to move index 3, 4 and 5 to the right which is 3 step and then insert 
the new element to blank space at index 3 which is 4 steps in total
-> worst case is N+1 step for N length array
```

// Deletion
```
After deletion at an index (1step), we need to shift other to the left.
Ex: delete at index 3, we have to shift 4 and 5 to left which  is 3 steps in total
-> worst case: N step 
```

// Single rule with Set:
// Reading: same as Array

//Searching: same as array
//Insertion:
```
the computer first needs to determine that this value
doesn’t already exist in this set—because that’s what sets do: 
they prevent duplicate data from being inserted into them
So, every insertion into a set first requires a search
worst case: 2N+1
```

//Deletion: same


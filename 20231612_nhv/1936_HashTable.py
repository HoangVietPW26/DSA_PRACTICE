"""
HashTable is the lost of paired value (key-value)
It have diff name in diff language : HashMap(Java), Dict(Python)
"""

thesaurus = {}

"""
Under the hood, a hash table stores its data in a bunch of cells in a row,
similar to an array. Each cell has a corresponding number
|  |  |  |  |  |  |  |  |  |  |  |
1  2  3  4  5  6  7  8  9  10 11 12
"""

thesaurus["bad"] = "evil"

"""
First, the computer applies the hash function to the key. Again, we’ll be using
the “multiplication” hash function described previously. So, this would compute as:
BAD = 2 * 1 * 4 = 8
Since our key ("bad") hashes into 8, the computer places the value ("evil") into
cell 8:
|  |  |  |  |  |  |  |"evil"  |  |  |  |
1  2  3  4  5  6  7  8        9  10 11 12

Now, let’s add another key-value pair:
thesaurus["cab"] = "taxi"
Again, the computer hashes the key:
CAB = 3 * 1 * 2 = 6
|  |  |  |  |  |"taxi  |  |"evil"  |  |  |  |
1  2  3  4  5  6       7  8        9  10 11 12
"""

#Hash Table look up
"""
thesaurus["bad"]
To find the value associated with "bad", the computer executes two simple
steps:
1. The computer hashes the key we’re looking up: BAD = 2 * 1 * 4 = 8.
2. Since the result is 8, the computer looks inside cell 8 and returns the
value stored there. In this case, that is the string, "evil".
O(1)

The whole premise of the hash table is that the key determines
the value’s location. But this premise only works in one direction: 
we use the key to find the value. 
The value does not determine the key’s location, so we
have no way to easily find any key without combing through all of them.

Come to think of it, where are the keys stored? In the previous diagrams, we
only saw how the values are stored in the hash table.
While this detail may vary from language to language, 
some languages store the keys next to the values themselves. 
This is useful in case of collisions, which I’ll discuss in the 
next section.
"""

#Dealing with collision
"""
thesaurus["dab"] = "pat"
First, the computer would hash the key:
DAB = 4 * 1 * 2 = 8
Then, it would try to add "pat" to our hash table’s cell 8:

Uh-oh. Cell 8 is already filled with "evil"—literally!
Trying to add data to a cell that is already filled is known as a collision. Fortunately, there are ways around it.
One classic approach for handling collisions is known as separate chaining.
When a collision occurs, instead of placing a single value in the cell, it places
in it a reference to an array.
Let’s look more carefully at a subsection of our hash table’s underlying data
storage:

|["bad"]["evil"]|["dab"]["pat"]|

This array contains subarrays where the first value is the word, and the second
value is its synonym.
Let’s walk through how a hash table lookup works in this case. If we look up:
thesaurus["dab"]
the computer takes the following steps:
1. It hashes the key: DAB = 4 * 1 * 2 = 8.
2. It looks up cell 8. The computer takes note that cell 8 contains an array
of arrays rather than a single value.
3. It searches through the array linearly, looking at index 0 of each subarray
until it finds our key ("dab"). It then returns the value at index 1 of the
correct subarray. -> O(N) 

Luckily, most programming languages implement hash tables and handle
these details for us. However, by understanding how it all works under the
hood, we can appreciate how hash tables eke out O(1) performance.

"""

"""
Hash table can be use to increase speed by convet array to has for ex
"""

#Prob1
"""
Write a function that returns the intersection of two arrays. 
The intersection is a third array that contains all values contained within the first two
arrays. 
For example, the intersection of [1, 2, 3, 4, 5] and [0, 2, 4, 6, 8] 
is [2, 4].
Your function should have a complexity of O(N)
"""

def intersection_of_two_arrays(arr1: list, arr2: list) -> list:
    dictionary = {}
    intersection = []
    for i in arr1:
        dictionary[i] = True
    for i in arr2:
        if dictionary[i]:
            intersection.append(i)
    return intersection


#Prob2
"""
Write a function that accepts an array of strings and returns the first
duplicate value it finds. For example, if the array is 
["a", "b", "c", "d", "c", "e", "f"], the function should return "c", 
since it’s duplicated within the array.
(You can assume that there’s one pair of duplicates within the array.)
"""
def first_dup_value_of_string(arr: list) -> str:
    dictionary = {}
    for s in arr:
        if not dictionary[s]:
            dictionary[s] = True
        else:
            return s
    return ""

#prob3
"""
Write a function that accepts a string that contains all the letters of the
alphabet except one and returns the missing letter. For example, the string,
"the quick brown box jumps over a lazy dog" contains all the letters of the alphabet
except the letter, "f". The function should have a time complexity of O(N)
"""
def missing_letter(s: str) -> str:
    alphabet_string = "abcdefghijklmnopqrstuvwxyz"
    dictionary = {}
    for i in s:
        dictionary[i] = True
    for i in alphabet_string:
        if not dictionary[i]:
            return i
    return ""

#prob4
"""
Write a function that returns the first non-duplicated character in a string.
For example, the string, "minimum" has two characters that only exist
once—the "n" and the "u", so your function should return the "n", since it
occurs first. The function should have an efficiency of O(N).
"""
def first_non_dup_letter(s: str) -> str:
    dictionary = {} 
    for c in s:
        if dictionary[c]:
            return c
        else:
            dictionary[c] = True
    return ""
    


    


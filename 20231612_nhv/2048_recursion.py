

#Reading recursive code

"""
Factorial
"""

def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
"""
This code can look somewhat confusing at first glance. To walk through the
code to see what it does, here’s the process I recommend:
1. Identify the base case.
2. Walk through the function for the base case.
3. Identify the “next-to-last” case. 
This is the case just before the base case, as I’ll demonstrate momentarily.
4. Walk through the function for the “next-to-last” case.
5. Repeat this process by identifying the case 
before the one you just analyzed, and walking though the function 
for that case.
"""

"""
Base case: recursion not call itself: n=1
factorial(1) return 1

nex-to-last: factorial(2)
factorial(2) return 2*factorial(1) -> 2*1

factorial(3) -> 3*factorial(2) -> 3*2*1
factorial(n) -> n*(n-1)*(n-2)*...*1 -> n!
"""

"""
Computer deal with recusion via Call Stack

fac(1)
fac(2)
fac(3)
-> If infinite recursion -> stack overflow
"""

"""
Here is an array containing both numbers as well as other arrays, which
in turn contain numbers and arrays:
array = [   1,
            2,
            3,
            [4, 5, 6],
            7,
            [8,
            [9, 10, 11,
            [12, 13, 14]
            ]
            ],
            [15, 16, 17, 18, 19,
            [20, 21, 22,
            [23, 24, 25,
            [26, 27, 29]
            ], 30, 31
            ], 32
            ], 33
            ]
Write a recursive function that prints all the numbers (and jút number)
"""
array = [   1,
            2,
            3,
            [4, 5, 6],
            7,
            [8,
            [9, 10, 11,
            [12, 13, 14]
            ]
            ],
            [15, 16, 17, 18, 19,
            [20, 21, 22,
            [23, 24, 25,
            [26, 27, 29]
            ], 30, 31
            ], 32
            ], 33
            ]
def write_numbers(arr: list):
    for element in arr:
        if isinstance(element, list):
            write_numbers(element)
        else:
            print(element)
# writing recusive, recursive can be use when we repeatly execute smthing
# Trick 1: add extra parameters
def double_array(array):
    index = 0
    while (index < len(array)):
        array[index] *= 2
        index += 1

def double_array(array, index=0):
    # Base case: when the index goes past the end of the array
    if index >= len(array):
        return
    array[index] *= 2
    double_array(array, index + 1)
# recursive use in calculation base on subproblems, 
"""
The Top-Down Thought Process
If you haven’t done a lot of top-down recursion before, it takes time and
practice to learn to think in this way. However, I found that when tackling a
top-down problem, it helps to think the following three thoughts:
1. Imagine the function you’re writing has already been implemented by
someone else.
2. Identify the subproblem of the problem.
3. See what happens when you call the function on the subproblem and go
from there.
"""
#Prob Array sum
"""
Sum of all element [1,2,3,4,5]
imagine we have the sum function
-> subprob: [2,3,4,5]
-> 1 + sum(2,3,4,5)
base case: only one element in the list
"""
def sum_of_array(arr: list) -> int:
    return arr[0] if len(arr) == 1 else \
            arr[0] + sum_of_array(arr[1, len(arr)-1])

#String reversal

"""
Let’s try another example. We’re going to write a reverse function 
that reverses a string. So, if the function accepts the argument "abcde",
it’ll return "edcba".

subprob: "bcde"
reverse("bcde") -> edcb + "a"
base case: str with len(1)
"""

def reverse_string(s: str) -> str:
    return s[0] if len(s) == 1 else \
            reverse_string(s[1:]) + s[0]

# count x in string
"""
 Let’s write a function called count_x
that returns the number of “x’s” in a given string. 
If our function is passed the string, "axbxcxd", it’ll return 3,
since there are three instances of the character “x.

subprob: "xbxcxd"
call_x("xbxcxd") + 0 (a)
call_x("bxcxd") + 1 (x)
base case str has 1 elemt 
"""

def count_x(s:str) -> str:

    if len(s) == 0:
        return 0
    if s[0] == "x": 
        return 1 + count_x(s[1:])
    else:
        return count_x(s[1:]) # duplicate reursive call, fix in the next section

#Staircase problem
"""
Let’s say we have a staircase of N steps, and a person has the ability to climb
one, two, or three steps at a time. How many different possible “paths” can
someone take to reach the top? Write a function that will calculate this for N
steps.

example: N = 11
subprob :N =10
-> posspath(10) -> 9 and 8 can jump to 11 as well
-> posspath(10) + posspath(9) + posspath(8)
-> posspath(9) + poss(8) +poss(7)
-> recursive

basecase: tricky -> hard code the bottome n=1,2,3 or rig the system
"""
def num_of_paths(n:int) -> int:
    if n <=0 : return 0
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    return num_of_paths(n-3) + num_of_paths(n-2) + num_of_paths(n-1)

"""
We know that we definitely want the result of number_of_paths(1) to be 1, so we’ll
start with the base case of:
return 1 if n == 1
Now, we know that we want number_of_paths(2) to return 2, but we don’t have
to create that base case explicitly. Instead, we can take advantage of the fact
that number_of_paths(2) will compute as number_of_paths(1) + number_of_paths(0) +
number_of_paths(-1). Since number_of_paths(1) returns 1, if we made number_of_paths(0)
also return 1, and number_of_paths(-1) return 0, we’d end up with a sum of 2,
which is what we want.

Let’s move onto number_of_paths(3), which will return the sum of number_of_paths(2)
+ number_of_paths(1) + number_of_paths(0). We know that we want the result to be
4, so let’s see if the math works out. We already rigged number_of_paths(2) to
return 2. number_of_paths(1) will return 1, and number_of_paths(0) will also return
1, so we end up getting the sum of 4, which is just what we need.
"""
def number_of_paths_rig(n):
    if n < 0:
        return 0 
    if n == 1 or n == 0:
        return 1 
    return number_of_paths_rig(n - 1) + number_of_paths_rig(n - 2) \
        +number_of_paths_rig(n - 3)


#Anagram generation
"""
anagram of "abcd"
anagram("bcd") + "a" in all posible position
anagram("cd") + "b" in all possible solution
base case: len 1
"""

def find_anagrams(s: str) -> list:
    anagrams  = []
    if len(s) == 1:
        return [s]
    sub_anagrams = find_anagrams(s[1:])
    for sub_anagram in sub_anagrams:
        for i in range(len(sub_anagram)):
            anagrams.append(sub_anagram[0:i] + s[0] + sub_anagram[i:])
        # we still lack of the case append to the end
        anagrams.append(sub_anagram + s[0])
    return anagrams



"""
Use recursion to write a function that accepts an array of strings and
returns the total number of characters across all the strings. For example,
if the input array is ["ab", "c", "def", "ghij"], 
the output should be 10 since there are 10 characters in total.
"""

def total_number(arr: list) -> int:
    if len(arr) == 1:
        return len(arr[0])
    return len(arr[0]) + total_number(arr[1:])

"""
Use recursion to write a function that accepts an array of numbers and
returns a new array containing just the even numbers.
"""
def find_even(arr: list) -> list:
    if len(arr) == 0:
        return []
    even_list = find_even(arr[1:]) # slicing out rage not cause error, it return []
    if arr[0] % 2 == 0:
        return [arr[0]] + even_list
    else:
        return even_list
    
"""
There is a numerical sequence known as “Triangular Numbers.” The
pattern begins as 1, 3, 6, 10, 15, 21, and continues onward with the Nth
number in the pattern, which is N plus the previous number. For example,
the 7th number in the sequence is 28, since it’s 7 (which is N) plus 21
(the previous number in the sequence). Write a function that accepts a
report erratum • discuss
Wrapping Up • 181number for N and returns the correct number from the series. That is, if
the function was passed the number 7, the function would return 28

N = 7 -> 7 + triag(6) -> 7 + 21
N = 6 -> 6 + troag(5) -> 6 + 15

base case: Tricky
N = 1 -> triag = 1 -> 1+trige(0) -> triage(0) = 0
N = 2 -> 2 + triage(1)  -> 3
"""

def triangular_number(pos: int) -> int:
    if pos <= 0: return 0
    if pos == 1: return 1
    return pos + triangular_number(pos-1)


"""
Use recursion to write a function that accepts a string and returns the
first index that contains the character “x.” For example, the string,
"abcdefghijklmnopqrstuvwxyz" has an “x” at index 23. To keep things simple,
assume the string definitely has at least one “x.

at least one x -> len must be >= 1
abcxd -> a + fx(bcxd) -> 1 + 2
base case "x"
"""
def first_index_of_x(s: str) -> int:
    if s[0] == "x":
        return 0
    else:
        return 1 + first_index_of_x(s[1:])

"""
This problem is known as the “Unique Paths” problem: Let’s say you have
a grid of rows and columns. Write a function that accepts a number of rows
and a number of columns, and calculates the number of possible “shortest”
paths from the upper-leftmost square to the lower-rightmost square.
shortest: combo of 1 step downward and 1 step rightward

3*4
bot right: come from above and left (2 ways)
above: above and left (2ways)
left: above and left (2ways)
on top or at left mose -> onle come form above or left (1wasy) 
to reach to: go thorigh all row
to reach right most: go through a column
top left: no where to cpme from
"""

def unique_paths(row: int, col: int) -> int:

    if row == 1 or col == 1:
        return 1
    else:
        return 2 + unique_paths(row-1, col) + unique_paths(row, col-1)

if __name__ == "__main__":
    write_numbers(array)
    print(count_x("xbxcxd"))
    print(num_of_paths(11))
    print(find_anagrams("abcd"))
    print(total_number(["ab", "c", "def", "ghij"]))
    print(find_even([2]))
    print(triangular_number(7))
    print(first_index_of_x("abcdefghijklmnopqrstuvwxyz"))
    print(unique_paths(3,7))
    

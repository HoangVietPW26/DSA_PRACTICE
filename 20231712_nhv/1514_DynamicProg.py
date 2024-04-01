
#Recusion problem

"""
Uneccessary recursive call
"""

def max(array):
    # Base case - if the array has only one element, it is
    # by definition the greatest number:
    if array.length == 1:
        return array[0] 
    # Compare the first element with the greatest element
    # from the remainder of the array. If the first element
    # is greater, return it as the greatest number:
    if array[0] > max(array[1, array.length - 1]):
        return array[0]
    else:
        return max(array[1, array.length - 1])
    
# duplicate recursive called, solved by save max in a variable

def max(array):
    if array.length == 1:
        return array[0]

    maximum = max(array[1, array.length-1])
    if array[0] > maximum:
        return array[0]
    else:
        return maximum

"""
First : O(2^n): call it self twice each run
Second : O(N), max recursive with N*N
"""

#Overlapping Subproblem
def fib(n):
    # The base cases are the first two numbers in the series:
    if n == 0 or n == 1:
        return n
    # Return the sum of the previous two Fibonacci numbers:
    return fib(n - 2) + fib(n - 1) #O(2^N)

"""
fib(n-1) will call fib(n-2) too.
Well, it seems that we’re at a dead end. Our Fibonacci example requires us
to make many overlapping function calls, and our algorithm oozes along at
a pace of O(2^N). There’s just nothing we can do.
Or is there?

Dynamic programming is the process of optimizing recursive
problems that have overlapping subproblems.

The first technique is something called memoization
Essentially, memoization reduces recursive calls by remembering previously
computed functions.
(In this respect, memoization really is like its 
similarsounding word memorization.)

In our Fibonacci example, the first time fib(3) is called, the function does its
computation and returns the number 2. However, before moving on, the
function stores this result inside a hash table. The hash table will look
something like this:
{3: 2}
This indicates that the result of fib(3) is the number 2.
Similarly, our code will memoize the results of all new computations it encounters. After encountering fib(4), fib(5), and fib(6), for example, our hash table will
look like this:
{
3: 2,
4: 3,
5: 5,
6: 8
}
report erratum • discuss
Dynamic Programming through Memoization • 191Now that we have this hash table, we can use it to prevent future recursive
calls. Here’s the way this works:
Without memoization, in call stack fib(4) would normally call fib(3) 
and fib(2), which in turn make their own recursive calls. 
Now that we have this hash table, we can approach things differently. 
Instead of fib(4) just blithely calling fib(3), for example, 
it first checks the hash table to see if the result of fib(3) has already
been computed. Only if the 3 key is not in the hash table does the function
proceed to call fib(3).
"""

def fib(n, memo):
    if n == 0 or n == 1:
        return n

    # Check the hash table (called memo) to see whether fib(n)
    # was already computed or not:
    if not memo.get(n):
    # If n is NOT in memo, compute fib(n) with recursion
    # and then store the result in the hash table:
        memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    # By now, fib(n)'s result is certainly in memo. (Perhaps
    # it was there before, or perhaps we just stored it there
    # in the previous line of code. But it's certainly there now.)
    # So let's return it:
    return memo[n]

"""
I mentioned earlier that dynamic programming can be achieved through one of
two techniques. We looked at one technique, memoization, which is quite nifty.
The second technique, known as going bottom-up, is a lot less fancy and may
not even seem like a technique at all. All going bottom-up means is to ditch
recursion and use some other approach (like a loop) to solve the same problem.
"""

def fib(n):
    if n == 0:
        return 0
    # a and b start with the first two numbers in the
    # series, respectively:
    a = 0
    b = 1
    # Loop from 1 until n:
    for i in range(1, n):
    # a and b each move up to the next numbers in the series.
    # Namely, b becomes the sum of b + a, and a becomes what b used to be.
    # We utilize a temporary variable to make these changes:
        temp = a
        a = b
        b = temp + a
    return b

"""
The following function accepts an array of numbers and returns the sum,
as long as a particular number doesn’t bring the sum above 100. If adding
a particular number will make the sum higher than 100, that number is
ignored. However, this function makes unnecessary recursive calls. Fix
the code to eliminate the unnecessary recursion:
"""

def add_until_100(array):
    if len(array) == 0:
        return 0 
    if array[0] + add_until_100(array[1, array.length - 1]) > 100:
        return add_until_100(array[1, array.length - 1])
    else:
        return array[0] + add_until_100(array[1, array.length - 1])

#dynamic prog
def add_until_100_dp(arr: list) -> int:
    if len(arr) == 0:
        return 0
    total = add_until_100(arr[1: len(arr)-1])
    if arr[0] + total > 100:
        return total
    else:
        return arr[0]
    
"""
The following function uses recursion to calculate the Nth number from
a mathematical sequence known as the “Golomb sequence.” It’s terribly
inefficient, though! Use memoization to optimize it. (You don’t have to
actually understand how the Golomb sequence works to do this exercise.)
"""

def golomb(n):
    if n == 1:
        return 1 
    return 1 + golomb(n - golomb(golomb(n - 1)))


def golomb(n, memo):
    if n==1:
        return 1
    if not memo.get(n):
        memo[n] = 1 + golomb(n - golomb(golomb(n - 1, memo), memo), memo)
    return memo[n]

"""
Here is a solution to the “Unique Paths” problem from an exercise in the
previous chapter. Use memoization to improve its efficiency:
"""

def unique_paths(row: int, col: int) -> int:

    if row == 1 or col == 1:
        return 1
    else:
        return unique_paths(row-1, col) + unique_paths(row, col-1)
    
def unique_paths_dp(row: int, col: int, memo) -> int:
    if row == 1 or col == 1:
        return 1
    if not (memo.get((row,col))):
        memo[(row,col)] = unique_paths(row-1, col) + unique_paths(row, col-1)
    return memo[(row,col)]
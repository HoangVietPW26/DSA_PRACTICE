# This is the theory about BigO
""" 
Resoure: 
1. A Common Guide To DSA - Jay Wengrow - 2nd
2. Cracking Coding Interview - Gayle Laakmann MacDonell -6th
"""

"""
Big O represent for how many steps an algorithm takes for N data elements
Often reder to the worst case
Ex: Linear Search, best case: O(1), worst case O(N)
"""

"""
O(1): step not increase no matter data element increase
O(N): step increase linearly with num of data element
O(logN): algo take as many steps to halve data elements until 1
O(1) < O(logN) < O(N)
"""

def isLeapYear(year) :
     return (year % 100 == 0 and year % 400 == 0) \
        or (year % 4 == 0 and year % 100 != 0)

# O(1)

def arraySum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
    return sum

#O(N): step increase linerly with array length





from typing import List
"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

 

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.

"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxProdLength = 0
        def getMask(word):
            mask = 0
            for c in word: #O(26)
                mask |= 1 << (ord(c) - ord('a'))
            return mask

        mask = []
        for word in words: #O(N)
            mask.append(getMask(word))

        for i in range(len(words)): #O(n^2)
            for j in range(i, len(words)):
                if not mask[i] & mask[j]:
                    maxProdLength = max(maxProdLength, len(words[i])*len(words[j]))
        
        return maxProdLength
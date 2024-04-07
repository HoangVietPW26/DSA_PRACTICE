from typing import List
"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 
Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def checkWord(m, n, startPos, gone = set()):
            if m<0 or m>=len(board) or n<0 or n>=len(board[0]):
                return False
            if (m,n) in gone:
                return False
            if board[m][n] != word[startPos]:
                return False
            if board[m][n] == word[startPos] and startPos == len(word)-1:
                return True
            if board[m][n] == word[startPos]:
                gone.add((m,n))
                down =  checkWord(m+1,n, startPos+1, gone) 
                up = checkWord(m-1,n, startPos+1, gone) 
                right = checkWord(m,n+1, startPos+1, gone)
                left =  checkWord(m,n-1, startPos+1, gone)
                if down or up or left or right:
                    return True
                else:
                    gone.remove((m,n))
                    return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if checkWord(i,j,0,set()):
                        return True
        return False
                    
        
# Summary
# We need to find the largest square comprising of all ones in the given m \times nm×n matrix.
# In other words we need to find the largest set of connected ones in the given matrix that forms a square.
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

# Example:

# Input: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# Output: 4

# Use dp (i,j) to represent the maximum side length of a square with (i,j) as the lower right corner and containing only 1
# For each position (i,j) check the value of that position in the matrix:
# If the value of the position is 0, then dp (i,j)= 0, because the current position cannot be in a square of 1;
# If the value of the position is 1, then the value of dp(i,j)  is determined by the dp values of the three adjacent positions above, left, and upper left.
# Specifically, the element value of the current position is equal to the minimum value of the three adjacent positions plus 1.
# The state transition equation is as follows:

#   dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1

# In addition, boundary conditions need to be considered.
# If at least one of ii and JJ is 0, the side length of the largest square in the lower right corner with position  (I,j) can only be 1, so dp(i,j)= 1

# Here is an example to illustrate.The original matrix is as follows.
# 0 1 1 1 0
# 1 1 1 1 0
# 0 1 1 1 1
# 0 1 1 1 1
# 0 0 1 1 1
# The corresponding DP values are as follows.
# 0 1 1 1 0
# 1 1 2 2 0
# 0 1 2 3 1
# 0 1 2 3 2
# 0 0 1 2 3

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        
        maxSquare = maxSide * maxSide
        return maxSquare

# Complexity analysis

# Time complexity: O(mn), where m and n are the number of rows and columns of the matrix.
# You need to iterate over each element of the original matrix to calculate the value of the dp.

# Space complexity: O(mn), where m and n are the number of rows and columns of the matrix.
# Creates a matrix dp of the same size as the original matrix.

# Since the  dp(i,j) in the state transition equation is determined by the dp values of the three adjacent positions 
# above, left and upper left, two one-dimensional arrays can be used for state transition, and the space complexity can be optimized to O(n).

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if(not matrix):
            return 0
        m=len(matrix)
        n=len(matrix[0])
        res=0
        pre=0
        dp=[0]*(n+1) 
        for i in range(0,m):
            for j in range(1,n+1):
                tmp=dp[j]
                if(matrix[i][j-1]=="1"):
                    dp[j]=min(pre,dp[j-1],dp[j])+1
                    res=max(dp[j],res)
                else:
                    dp[j]=0
                pre=tmp
            pre=0
        return res*res



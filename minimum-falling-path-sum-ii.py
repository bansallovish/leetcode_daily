class Solution(object):
    def minFallingPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        for i in range(1, n):
            min_val = second_min_val = float('inf')
            min_index = -1

            for j in range(n):
                if grid[i - 1][j] < min_val:
                    second_min_val = min_val
                    min_val = grid[i - 1][j]
                    min_index = j
                elif grid[i - 1][j] < second_min_val:
                    second_min_val = grid[i - 1][j]

            for j in range(n):
                if j != min_index:
                    grid[i][j] += min_val
                else:
                    grid[i][j] += second_min_val

            # print(grid[i])

        return min(grid[-1])
        

obj1=Solution()        
print(13,obj1.minFallingPathSum2([[1,2,3],[4,5,6],[7,8,9]]))
print(13,obj1.minFallingPathSum2([[1,2,3,1],[4,5,6,1],[7,8,9,1],[4,5,6,1]]))
print(13,obj1.minFallingPathSum2([[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2]]))
print(-268,obj1.minFallingPathSum([[-37,51,-36,34,-22],[82,4,30,14,38],[-68,-52,-92,65,-85],[-49,-3,-77,8,-19],[-60,-71,-21,-62,-73]]))
print(-268,obj1.minFallingPathSum2([[-37,51,-36,34,-22],[82,4,30,14,38],[-68,-52,-92,65,-85],[-49,-3,-77,8,-19],[-60,-71,-21,-62,-73]]))
# print(13,obj1.minFallingPathSum([[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2],[2,2,1,2,2]]))
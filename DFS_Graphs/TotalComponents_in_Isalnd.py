# The above code will solve the Total Components  in each Island and 
"""
   1. we can then apply set operation to find the distinct Island 
   2. we can  find the biggest and Smallest Island as well .
   3. We can also find the total number of connected components - algo - just collect all components and count islandsize>1 - we have the answer.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        count = 0 
        result=[]
        #print(comp)
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 1:
                return 0
            
            # marking it with 0 here to avoid loop 
            grid[row][col] = 0
            size = 1 

            size+=dfs(row-1, col)
            size+=dfs(row+1, col)
            size+=dfs(row, col-1)
            size+=dfs(row, col+1)
            return size

        sizes = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    s = dfs(row, col)
                    if s > 0:
                        islands += 1
                        sizes.append(s)
                
        print(sizes)
        return islands


grid = [[1,1,0,1],
        [1,1,0,0]]
print(Solution().numIslands(grid))

"""
With Dictionary 
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        count = 0 
        result=[]
        #print(comp)
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 1:
                return 0
            
            # marking it with 0 here to avoid loop 
            grid[row][col] = 0
            size = 1 

            size+=dfs(row-1, col)
            size+=dfs(row+1, col)
            size+=dfs(row, col-1)
            size+=dfs(row, col+1)
            return size

        sizes = {}
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    s = dfs(row, col)
                    if s > 0:
                        islands += 1
                        sizes[f"{islands}"] = s
                
        print(sizes)
        return islands
        
grid = [[1,1,0,1],
        [1,1,0,0]]
        
print(Solution().numIslands(grid))
"""

#Solution to 3rd Problem Total Connected components (just connected components)
"""
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        count = 0 
        result=[]
        #print(comp)
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != 1:
                return 0
            
            # marking it with 0 here to avoid loop 
            grid[row][col] = 0
            size = 1 

            size+=dfs(row-1, col)
            size+=dfs(row+1, col)
            size+=dfs(row, col-1)
            size+=dfs(row, col+1)
            return size

        sizes = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    s = dfs(row, col)
                    if s > 0:
                        islands += 1
                        sizes.append(s)
                
        #print(sizes)
        
        connectedComp = 0
        for s in sizes:
            if s>1:
                connectedComp+=1
        print(connectedComp)
        
        return islands


grid = [[1,1,0,1],
        [1,1,0,0],
        [0,0,1,1],
        [1,1,0,0],
        [0,0,1,1]]

print(Solution().numIslands(grid))

"""






class Solution:
    def islandPerimeter(self, grid):
        islands = 0
        neighbors = 0

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    islands += 1

                    # Check down
                    if i + 1 < rows and grid[i + 1][j] == 1:
                        neighbors += 1

                    # Check right
                    if j + 1 < cols and grid[i][j + 1] == 1:
                        neighbors += 1

        return islands * 4 - neighbors * 2
        
    
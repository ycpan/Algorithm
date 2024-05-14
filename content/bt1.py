def numIslands(grid):
    if not grid:
        return 0
    num_of_islands = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                num_of_islands += 1
    return num_of_islands
def dfs(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
        return
    grid[i][j] = '0'  # 标记为已访问
    dfs(grid, i + 1, j)  # 向下探索
    dfs(grid, i - 1, j)  # 向上探索
    dfs(grid, i, j + 1)  # 向右探索
    dfs(grid, i, j - 1)  # 向左探索
# 示例1
grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(numIslands(grid1))  # 输出应为1
# 示例2
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(numIslands(grid2))  # 输出应为3

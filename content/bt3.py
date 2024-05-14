from collections import deque
def oranges_rotting(grid):
    m, n = len(grid), len(grid[0])
    fresh_oranges = 0
    queue = deque()
    # 遍历网格，统计新鲜橘子和腐烂橘子的位置
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_oranges += 1
    # 初始化分钟数
    minutes = 0
    # 四个方向
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 当队列不为空或有新鲜橘子时，继续
    while queue and fresh_oranges > 0:
        minutes += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
                    fresh_oranges -= 1
    # 如果还有新鲜橘子，返回 -1
    if fresh_oranges > 0:
        return -1
    else:
        return minutes
# 测试示例
example1 = [[2,1,1],[1,1,0],[0,1,1]]
example2 = [[2,1,1],[0,1,1],[1,0,1]]
example3 = [[0,2]]
oranges_rotting(example1), oranges_rotting(example2), oranges_rotting(example3)
(4, -1, 0)

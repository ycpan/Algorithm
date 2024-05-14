def can_finish(numCourses, prerequisites):
    # 初始化邻接表
    adj = [[] for _ in range(numCourses)]
    # 初始化访问状态数组
    visited = [0] * numCourses
    # 构建邻接表
    for course, pre in prerequisites:
        adj[pre].append(course)
    # 深度优先搜索
    def dfs(node):
        import ipdb
        ipdb.set_trace()
        # 如果节点状态为 1，说明存在循环
        if visited[node] == 1:
            return False
        # 如果节点状态为 2，说明已经访问过，直接返回 True
        if visited[node] == 2:
            return True
        # 将节点状态设置为 1
        visited[node] = 1
        # 遍历所有邻居
        for neighbor in adj[node]:
            if not dfs(neighbor):
                return False
        # 将节点状态设置为 2
        visited[node] = 2
        return True
    # 对每个节点进行 DFS 遍历
    for i in range(numCourses):
        import ipdb
        ipdb.set_trace()
        if visited[i] == 0 and not dfs(i):
            return False
    return True
# 测试示例
#example1 = (2, [[1, 0]])
#can_finish(*example1) # True
example2 = (2, [[1, 0], [0, 1]])
can_finish(*example2)

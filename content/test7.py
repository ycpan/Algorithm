def exist(board, word):
    def backtrack(row, col, index):
        # 如果索引到达单词的末尾，说明找到了一个匹配
        import ipdb
        ipdb.set_trace()
        if index == len(word):
            return True
        # 边界检查和越界情况
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
            return False
        # 标记当前位置已经访问过
        temp, board[row][col] = board[row][col], '/'
        # 尝试上下左右四个方向
        found = backtrack(row + 1, col, index + 1) or \
                backtrack(row - 1, col, index + 1) or \
                backtrack(row, col + 1, index + 1) or \
                backtrack(row, col - 1, index + 1)
        # 回溯，恢复当前位置的字符
        board[row][col] = temp
        return found
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
    return False
# 示例
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))  # 输出：True

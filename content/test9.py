def solveNQueens(n):
    def is_valid(board, row, col):
        # 检查同一列
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # 检查左上对角线
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        # 检查右上对角线
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        return True
    def backtrack(board, row):
        import ipdb
        ipdb.set_trace()
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'
    result = []
    backtrack([['.' for _ in range(n)] for _ in range(n)], 0)
    return result
# 示例
n = 4
print(solveNQueens(n))

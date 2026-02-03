from collections import deque
from typing import List


def solve(board: List[List[str]]) -> None:
    """
    使用BFS解决被围绕的区域问题

    参数:
    board: 二维字符矩阵，由'X'和'O'组成

    返回:
    None: 原地修改矩阵
    """
    # 如果矩阵为空，直接返回
    if not board or not board[0]:
        return

    # 获取矩阵的行数和列数
    m, n = len(board), len(board[0])

    # 初始化队列用于BFS
    queue = deque()

    # 遍历四个边界，找到所有边界上的'O'
    # 上边界和下边界
    for i in [0, m - 1]:
        for j in range(n):
            if board[i][j] == 'O':
                # 标记边界上的'O'为'B'，并加入队列
                board[i][j] = 'B'
                queue.append((i, j))

    # 左边界和右边界（排除四个角，因为已经在上面的循环中处理过）
    for j in [0, n - 1]:
        for i in range(1, m - 1):
            if board[i][j] == 'O':
                # 标记边界上的'O'为'B'，并加入队列
                board[i][j] = 'B'
                queue.append((i, j))

    # 定义四个方向的偏移量
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 使用BFS遍历所有与边界相连的'O'
    while queue:
        i, j = queue.popleft()

        # 检查四个方向的邻居
        for dx, dy in directions:
            ni, nj = i + dx, j + dy

            # 如果邻居在矩阵范围内且为'O'
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                # 标记为'B'，表示与边界相连
                board[ni][nj] = 'B'
                queue.append((ni, nj))

    # 遍历整个矩阵，进行最终处理
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'B':
                # 恢复与边界相连的'O'
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                # 将被围绕的'O'改为'X'
                board[i][j] = 'X'


def print_board(board):
    """打印矩阵"""
    for row in board:
        print(row)
    print()


if __name__ == "__main__":
    # 示例输入
    test_cases = [
        # 测试用例 1: 原始示例
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ],

        # 测试用例 2: 所有元素都是'X'
        [
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ],

        # 测试用例 3: 所有元素都是'O'
        [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"]
        ],

        # 测试用例 4: 中间有被围绕的'O'
        [
            ["X", "X", "X", "X", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "X", "X", "O", "X"],
            ["X", "O", "O", "O", "X"],
            ["X", "X", "X", "X", "X"]
        ],

        # 测试用例 5: 复杂情况
        [
            ["X", "O", "X", "X", "O", "X"],
            ["O", "X", "O", "X", "O", "O"],
            ["X", "O", "X", "O", "X", "X"],
            ["O", "X", "O", "X", "O", "O"],
            ["X", "O", "X", "O", "X", "X"]
        ],

        # 测试用例 6: 单行矩阵
        [
            ["X", "O", "X", "O", "X"]
        ],

        # 测试用例 7: 单列矩阵
        [
            ["X"],
            ["O"],
            ["X"],
            ["O"],
            ["X"]
        ],

        # 测试用例 8: 大型矩阵
        [
            ["X", "O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X", "O", "X"]
        ]
    ]

    for i, board in enumerate(test_cases, 1):
        print(f"测试用例 {i}:")
        print("原始矩阵:")
        print_board(board)

        # 解决问题
        solve(board)

        print("处理后的矩阵:")
        print_board(board)
        print("=" * 50)

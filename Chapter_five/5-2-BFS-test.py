from collections import deque


def bfs_traverse(grid):
    """
    使用广度优先搜索遍历网格中与起点(0,0)字符相同的连通区域

    参数:
        grid: 二维列表，代表输入的字符网格

    返回:
        visited: 二维列表，访问矩阵，1表示被访问(同字符且连通)，0表示未访问
    """
    # 处理空网格情况
    if not grid or len(grid) == 0:
        return []

    # 获取网格的行数和列数
    rows = len(grid)
    cols = len(grid[0])

    # 初始化访问矩阵，全部置为0
    visited = [[0 for _ in range(cols)] for _ in range(rows)]

    # 定义四个遍历方向：右、下、左、上（按题目要求顺序）
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 获取起点字符（左上角单元格）
    start_char = grid[0][0]

    # 初始化队列并添加起点
    queue = deque()
    queue.append((0, 0))

    # 标记起点为已访问
    visited[0][0] = 1

    # 执行BFS遍历
    while queue:
        # 取出队列头部元素
        x, y = queue.popleft()

        # 遍历四个方向
        for dx, dy in directions:
            # 计算相邻单元格坐标
            nx = x + dx  # 新行坐标
            ny = y + dy  # 新列坐标

            # 检查相邻单元格是否在网格边界内
            if 0 <= nx < rows and 0 <= ny < cols:
                # 检查是否未被访问且与起点字符相同
                if visited[nx][ny] == 0 and grid[nx][ny] == start_char:
                    # 标记为已访问
                    visited[nx][ny] = 1
                    # 加入队列等待后续处理
                    queue.append((nx, ny))

    return visited


# 主程序逻辑
if __name__ == "__main__":
    # 读取输入行数
    m = int(input())

    # 读取网格数据
    grid = []
    for _ in range(m):
        line = input().strip()
        grid.append(line)

    # 调用BFS遍历函数
    result = bfs_traverse(grid)

    # 输出结果
    for row in result:
        print(str(row))

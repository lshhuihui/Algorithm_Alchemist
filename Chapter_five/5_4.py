from collections import deque
from typing import List, Tuple


def bfs_maze(maze: List[List[str]], start: Tuple[int, int], goal: Tuple[int, int]) -> int:
    """
    使用广度优先搜索(BFS)计算迷宫最短路径

    参数:
    maze: 二维字符列表，表示迷宫地图
    start: 元组，表示起点坐标 (row, col)
    goal: 元组，表示终点坐标 (row, col)

    返回:
    int: 最短路径长度，如果无法到达则返回-1
    """
    # 处理空迷宫的情况
    if not maze or not maze[0]:
        return -1

    # 获取迷宫的行数和列数
    rows, cols = len(maze), len(maze[0])

    # 初始化距离矩阵，记录每个单元格到起点的距离，初始值为-1（表示未访问）
    dist = [[-1] * cols for _ in range(rows)]

    # 初始化队列用于BFS
    queue = deque()

    # 定义四个方向的偏移量：上、右、下、左
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 将起点加入队列，并设置起点距离为0
    start_row, start_col = start
    dist[start_row][start_col] = 0
    queue.append((start_row, start_col))

    # 执行BFS
    while queue:
        # 从队列中取出一个单元格
        x, y = queue.popleft()

        # 如果当前单元格是终点，返回距离
        if (x, y) == goal:
            return dist[x][y]

        # 检查四个方向的相邻单元格
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # 检查相邻单元格是否在迷宫范围内
            if 0 <= nx < rows and 0 <= ny < cols:
                # 检查相邻单元格不是墙壁且未被访问
                if maze[nx][ny] != '#' and dist[nx][ny] == -1:
                    # 设置相邻单元格的距离
                    dist[nx][ny] = dist[x][y] + 1
                    # 将相邻单元格加入队列
                    queue.append((nx, ny))

    # 如果循环结束仍未找到终点，返回-1
    return -1


def main():
    """
    主函数：处理输入输出
    """
    # 读取第一行，获取迷宫的行数 N 和列数 M
    first_line = input().split()
    N = int(first_line[0])
    M = int(first_line[1])

    # 初始化迷宫地图
    maze = []
    start = None
    goal = None

    # 读取后续的 N 行数据
    for i in range(N):
        row = list(input().strip())
        maze.append(row)

        # 查找起点和终点
        for j in range(M):
            if row[j] == 'S':
                start = (i, j)
            elif row[j] == 'G':
                goal = (i, j)

    # 计算并输出最短路径长度
    result = bfs_maze(maze, start, goal)
    print(result)


if __name__ == "__main__":
    main()


'''
3 3
S#.
.#.
..G
'''
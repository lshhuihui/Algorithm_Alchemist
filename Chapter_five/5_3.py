def main():
    # 读取输入的第一行，获取两个整数 N 和 M，分别表示矩阵的行数和列数
    N, M = map(int, input().split())
    # 初始化一个二维列表 grid，大小为 N × M，用于存储矩阵数据
    grid = []
    # 对于 i 从 0 到 N-1：
    for i in range(N):
        # 读取一行输入，包含 M 个数字（0 或 1），并存入 grid[i]
        row = list(map(int, input().split()))
        grid.append(row)
    # 初始化岛屿计数器 count 为 0
    count = 0
    # 对于 i 从 0 到 N-1：
    for i in range(N):
        # 对于 j 从 0 到 M-1：
        for j in range(M):
            # 如果 grid[i][j] 等于 1（表示陆地）：
            if grid[i][j] == 1:
                # count 增加 1
                count += 1
                # 调用 DFS 函数处理当前网格 grid 和位置 (i, j)，以及尺寸 N, M
                dfs(grid, i, j, N, M)
    # 输出 count
    print(count)


def dfs(grid, i, j, N, M):
    # 如果当前坐标 (i, j) 越界（即 i < 0 或 i >= N 或 j < 0 或 j >= M）或者 grid[i][j] 不等于 1：
    if i < 0 or i >= N or j < 0 or j >= M or grid[i][j] != 1:
        # 直接返回（递归终止条件）
        return
    # 将 grid[i][j] 设置为 0（标记为已访问，避免重复计算）
    grid[i][j] = 0
    # 递归处理四个方向：上、下、左、右
    dfs(grid, i - 1, j, N, M)  # 上
    dfs(grid, i + 1, j, N, M)  # 下
    dfs(grid, i, j - 1, N, M)  # 左
    dfs(grid, i, j + 1, N, M)  # 右


if __name__ == "__main__":
    main()

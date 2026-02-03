from collections import defaultdict, deque
def dfs(graph, start):
    """
    使用DFS遍历图
    参数:
    graph: 邻接表表示的图
    start: 起始顶点
    返回:
    visited: 按DFS顺序访问的顶点列表
    """
    visited = []  # 存储已访问的顶点
    stack = [start]  # 使用栈实现DFS
    while stack:
        # 弹出栈顶顶点
        vertex = stack.pop()
        # 如果顶点未被访问，处理它
        if vertex not in visited:
            visited.append(vertex)  # 标记为已访问
            # 将未访问的邻居压入栈
            # 注意：使用逆序以保证与递归DFS相同的顺序
            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

def bfs(graph, start):
    """
    使用BFS遍历图
    参数:
    graph: 邻接表表示的图
    start: 起始顶点
    返回:
    visited: 按BFS顺序访问的顶点列表
    """
    visited = []  # 存储已访问的顶点
    queue = deque([start])  # 使用队列实现BFS
    while queue:
        # 弹出队列前端顶点
        vertex = queue.popleft()
        # 如果顶点未被访问，处理它
        if vertex not in visited:
            visited.append(vertex)  # 标记为已访问
            # 将未访问的邻居加入队列
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

if __name__ == "__main__":
    # 从输入构建图
    graph = defaultdict(list)
    n = int(input())  # 读取顶点数量
    # 读取边的信息
    for _ in range(n - 1):  # 对于n个顶点的树，有n-1条边
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)  # 无向图，添加双向边
    print("DFS遍历顺序:", dfs(graph, 0))
    print("BFS遍历顺序:", bfs(graph, 0))


"""
5
0 1
0 2
1 3
2 4

8
0 1
1 2
1 3
3 4
3 5
0 6
6 7
"""




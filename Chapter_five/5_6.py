graph = []
visited = []
stack = []
def dfs(node):
    """
    深度优先搜索函数，用于检测环并进行拓扑排序
    :param node: 当前访问的节点
    :return: 是否检测到环（True-无环，False-有环）
    """
    # 将当前节点标记为"访问中"
    visited[node] = 1
    # 遍历当前节点的所有邻居节点
    for neighbor in graph[node]:
        if visited[neighbor] == 0:  # 如果邻居节点未访问
            if not dfs(neighbor):  # 递归访问邻居节点
                return False  # 如果检测到环，返回False
        elif visited[neighbor] == 1:  # 如果邻居节点正在访问中（在DFS路径上）
            return False  # 检测到环，返回False
    # 当前节点的所有邻居都已处理完毕
    visited[node] = 2  # 标记为已访问
    stack.append(node)  # 将节点加入结果栈
    return True

def main():
    """
    主函数，处理输入并调用DFS算法解决问题
    """
    global graph, visited, stack  # 声明使用全局变量
    # 读取课程数量
    numCourses = int(input().strip())
    # 读取先修条件字符串，按空格分割
    s = input().split()
    prerequisites = []
    # 将输入的先修条件转换为整数对列表
    for i in range(0, len(s), 2):
        # 每两个数字组成一个先修条件对 [a_i, b_i]
        a = int(s[i])
        b = int(s[i + 1])
        prerequisites.append([a, b])
    # 构建邻接表表示的有向图
    graph = [[] for _ in range(numCourses)]
    # 初始化访问状态数组：0-未访问，1-访问中，2-已访问
    visited = [0] * numCourses
    # 初始化结果栈，用于存储拓扑排序结果
    stack = []
    # 填充邻接表
    for a, b in prerequisites:
        # 添加边 b->a，表示修完b才能修a
        graph[b].append(a)
    # 遍历所有课程节点
    for i in range(numCourses):
        if visited[i] == 0:  # 如果节点未访问
            if not dfs(i):  # 进行深度优先搜索
                # 等待用户按下空格键
                input("检测到环，无法完成课程安排。按空格键查看结果...")
                print("[]")  # 输出空数组
                return
    # 输出拓扑排序结果（栈的逆序）
    # 因为DFS是递归完成后才将节点入栈，所以栈顶是最后完成的课程
    # 我们需要的是从先修课程到后续课程的顺序，所以要反转栈
    result = stack[::-1]
    # 格式化输出为数组形式
    print("[" + ",".join(map(str, result)) + "]")

if __name__ == "__main__":
    main()

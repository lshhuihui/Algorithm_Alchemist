'''
①先把这个n*n矩阵内化出来
②定义2个方向  2 4 3 4，往右或往下(0,0) (0,1) (1,0)
③当从00-->01 / 10 ,靶子数目都+1
④只要没有到达终点就得一直走
    达到终点且靶子数目一至
    0,0==n-1,n-1

4
2 4 3 4
4 3 3 3

0 4 5 1 2 3 7 11 10 9 13 14 15

4行4列的矩阵，它的行标数字为4 3 3 3，列
标数字为2 4 3 4，每个格子值为0 1 2 ....14,15


  2 4 3 4
4 0 1 2 3
3 4 5 6 7
3 8 9 10 11
3 12 13 14 15

行走或者前进的规则，每个题不一样，那就需要总结当前这个题的行走规则

'''
move_roles = [(0,1), (1,0)]
# # 马走日字
# move_roles = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1), (-2,1), (-1,2)]
# # 五子棋
# move_roles = [(1,1), (1,-1), (-1,1), (-1,-1)]
def solve_path():
    N = int(input()) # 4
    north = list(map(int, input().split())) # 2 4 3 4
    west = list(map(int, input().split())) # 4 3 3 3
    # 迷宫的尺寸4
    # size = 4
    # 内部类 
    # 坐标转编号
    def coord_to_no(i,j):
        return i * N + j
    # 编号转坐标
    def num_to_coord(num):
        # (i,j)
        return (num // N, num % N) 
    
    # 开始深度搜索算法
    # 记录是否找到路径--没有找到
    found = False
    # 已访问的格子
    visited = [0] * (N * N)
    # 路径列表
    path = []
    # 开始深搜
    def dfs(current_num,step): # 当前格子编号，当前步数
        nonlocal found
        if found: # 找到路径了
            path.append(current_num) # 把当前格子编号加入路径列表
            visited[current_num] = 1 # 标记当前格子为已访问
            return path

        if step == N: # 如果当前步数等于N，说明已经走完了N步
            found = True # 找到路径了
            # 打印路径
            print(' '.join(map(str, path))) # join()是字符串特有的函数
            path.append(current_num) # 把当前格子编号加入路径列表
            visited[current_num] = 1 # 标记当前格子为已访问
            return path
        # 怎么让found变为True呢？怎么让step更新为N呢？ 7 --->（2,3）
        x,y = num_to_coord(current_num) # 当前格子坐标
        # 枚举下一步的格子（）往move_roles它去
        for dx,dy in move_roles:#  [(0,1), (1,0)]  # 枚举的意义在于确保了往右和往下都没有遗漏
            # 算出去向坐标
            nextx = x + dx
            nexty = y + dy
            # 一旦要动，就得先考虑边界
            if 0 <= nextx < N and 0 <= nexty < N: # 如果nextx(行)和nexty(列)都在N的范围内
                # 如果在范围内做什么？
                # 射一箭
                next_num = coord_to_no(nextx, nexty) # 下一个格子编号
                # 如果下一个格子没有被访问过，并且靶子数目满足要求
                if visited[next_num] != 1 and north[step] == (x - dx) * N + (y - dy) and west[step] == (x + dx) * N + (y + dy):
                    dfs(next_num, step + 1) # 递归
                    if found: # 如果找到路径了
                        return path
        # 如果无路可走---回溯
        path.pop() # 回溯
        visited[current_num] = 0 # 取消标记
    dfs(0,0)
    print(path)

solve_path()

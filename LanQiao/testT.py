from collections import deque
# 输入初始状态和目标状态
start = input().strip()
target = input().strip()
# BFS队列：(当前状态, 步数)
queue = deque()
queue.append((start, 0))
# 已访问过的状态，避免重复处理
visited = set()
visited.add(start)
# 移动的方向：相邻（±1）、隔1个（±2）、隔2个（±3）
moves = [-3, -2, -1, 1, 2, 3]
found = False
while queue:
    current, steps = queue.popleft()
    # 找到目标，输出步数
    if current == target:
        print(steps)
        found = True
        break
    # 找到空杯子的位置
    idx = current.index("*")
    # 枚举所有可能的移动
    for move in moves:
        # 计算青蛙的位置（青蛙跳到空杯子，所以青蛙的位置是 idx + move）
        frog_pos = idx + move
        # 判断青蛙位置是否合法
        if 0 <= frog_pos < len(current):
            # 转换为列表，方便交换
            current_list = list(current)
            # 交换青蛙和空杯子的位置
            current_list[idx], current_list[frog_pos] = (
                current_list[frog_pos],
                current_list[idx],
            )
            new_state = "".join(current_list)
            # 如果新状态没被访问过，加入队列
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))
if not found:
    print(-1)  # 理论上输入合法的话不会走到这



'''
跳到相邻的空杯子里。
隔着 1 只其它的青蛙（随便什么颜色）跳到空杯子里。
隔着 2 只其它的青蛙（随便什么颜色）跳到空杯子里。
输入描述
输入为 2 行，2 个串，表示初始局面和目标局面。我们约定，输入的串的长度不超过 15。
输出描述
输出要求为一个整数，表示至少需要多少步的青蛙跳。
输入
*WWBB
WWBB*
输出
2
'''
s = list(input())
t = list(input())
cnt = 0
result = []
# 标记是否找到目标，避免死循环
found = False
while s != t and not found:
    for i in range(len(s)):
        #相邻的是左边空杯子
        if s[i] == "*" and s[i-1] != "*"  :
            s[i],s[i-1] = s[i-1],s[i]
            cnt += 1 
            result.append(cnt)
            if s==t: 
                found = True
                break
        #相邻的是右边空杯子
        elif s[i] == "*" and s[i+1] != "*"  :
            s[i],s[i+1] = s[i+1],s[i]
            cnt += 1 
            result.append(cnt)
            if s==t:
                found = True
                break
        #隔着 1 只其它的青蛙（随便什么颜色）跳到空杯子里。    
        elif i-2 >= 0 and s[i-2] == "*" and s[i-1] != "*" :
            s[i],s[i-2] = s[i-2],s[i]
            cnt += 1 
            result.append(cnt)
            if s==t:
                found = True
                break
            
        #隔着 1 只其它的青蛙（随便什么颜色）跳到空杯子里。   
        elif i+2 <len(s) and s[i+2] == "*" and s[i+1] != "*" :
            s[i],s[i+2] = s[i+2],s[i]
            cnt += 1
            result.append(cnt)
            if s==t:
                found = True
                break
        #隔着 2 只其它的青蛙（随便什么颜色）跳到空杯子里。
        elif i-3 >= 0 and s[i-3] == "*" and s[i-2] != "*" and s[i-1] != "*" :
            s[i],s[i-3] = s[i-3],s[i]
            cnt += 1
            result.append(cnt)
            if s==t:
                found = True
                break
        #隔着 2 只其它的青蛙（随便什么颜色）跳到空杯子里。
        elif i+3 <len(s) and s[i+3] == "*" and s[i+2] != "*" and s[i+1] != "*" :
            s[i],s[i+3] = s[i+3],s[i]
            cnt += 1
            result.append(cnt)
            if s==t:
                found = True
                break
                
            
new_result = sorted(result,reverse= False)
print(new_result[0])
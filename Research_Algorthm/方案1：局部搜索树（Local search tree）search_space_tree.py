import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from collections import deque

# ============ 辅助函数 ============
def find_blank(state):
    """找到空白格(-1)的位置"""
    return state.index(-1)

def get_neighbors(state):
    """获取所有可能的相邻状态"""
    neighbors = []
    blank_idx = find_blank(state)
    row, col = blank_idx // 3, blank_idx % 3
    
    directions = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]
    
    for dr, dc, name in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = state.copy()
            new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
            neighbors.append((new_state, name))
    return neighbors

class TreeNode:
    def __init__(self, state, depth=0, parent=None, move_dir=""):
        self.state = state
        self.depth = depth
        self.parent = parent
        self.move_dir = move_dir
        self.children = []
        
    def add_child(self, child_state, move_dir):
        if self.parent and child_state == self.parent.state:
            return None
        child = TreeNode(child_state, self.depth + 1, self, move_dir)
        self.children.append(child)
        return child

def build_tree(root_state, max_depth=2):
    """构建搜索树到指定深度"""
    root = TreeNode(root_state, 0)
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node.depth >= max_depth:
            continue
        neighbors = get_neighbors(node.state)
        for next_state, direction in neighbors:
            if node.parent and next_state == node.parent.state:
                continue
            child = node.add_child(next_state, direction)
            if child:
                queue.append(child)
    return root

# ============ 绘图函数 ============
def draw_matrix(ax, center_x, center_y, state, size=0.8, highlight=False, 
                label=None, label_color='black', fontsize=12):
    """绘制状态矩阵"""
    cell_size = size / 3
    start_x = center_x - size / 2
    start_y = center_y - size / 2
    
    matrix = [state[i:i+3] for i in range(0, 9, 3)]
    
    # 高亮效果
    if highlight:
        rect = FancyBboxPatch((start_x - 0.05, start_y - 0.05), size + 0.1, size + 0.1,
                              boxstyle="round,pad=0.02", facecolor='#E8F8F5', 
                              edgecolor='#27AE60', linewidth=3)
        ax.add_patch(rect)
    else:
        # 阴影
        shadow = FancyBboxPatch((start_x + 0.02, start_y - 0.02), size, size,
                               boxstyle="round,pad=0.01", facecolor='gray', alpha=0.2)
        ax.add_patch(shadow)
        rect = FancyBboxPatch((start_x, start_y), size, size,
                              boxstyle="round,pad=0.01", facecolor='white', 
                              edgecolor='#2C3E50', linewidth=2)
        ax.add_patch(rect)
    
    # 绘制格子
    for row in range(3):
        for col in range(3):
            x = start_x + col * cell_size
            y = start_y + (2-row) * cell_size  # 注意：matplotlib y轴向上，反转行
            
            # 交替背景
            if (row + col) % 2 == 0:
                ax.add_patch(plt.Rectangle((x, y), cell_size, cell_size, 
                                          facecolor='#F8F9FA', edgecolor='#BDC3C7', linewidth=1))
            else:
                ax.add_patch(plt.Rectangle((x, y), cell_size, cell_size, 
                                          facecolor='white', edgecolor='#BDC3C7', linewidth=1))
            
            # 数字
            num = matrix[row][col]
            text = str(num)
            color = '#E74C3C' if num == -1 else '#2C3E50'
            weight = 'bold' if num == -1 else 'normal'
            ax.text(x + cell_size/2, y + cell_size/2, text, 
                   ha='center', va='center', fontsize=fontsize, 
                   color=color, weight=weight)
    
    # 标签
    if label:
        ax.text(center_x, start_y - 0.15, label, ha='center', va='top', 
               fontsize=11, color=label_color, weight='bold')

# ============ 主程序 ============
if __name__ == "__main__":
    # 设置中文字体（如果需要显示中文，改为 'SimHei' 或 'Microsoft YaHei'）
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['axes.unicode_minus'] = False
    
    # 当前状态（根节点）
    current_state = [0, 1, 2, 3, 4, 5, 6, -1, 7]
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, -1]
    
    # 构建搜索树
    root = build_tree(current_state, max_depth=2)
    
    # 创建画布
    fig, ax = plt.subplots(figsize=(16, 10), dpi=150)  # 你可以调高dpi获得更高清图像
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.set_facecolor('#FAFBFC')
    
    # 标题
    ax.text(8, 9.5, 'Solution 1: Local Search Tree (Depth = 2)', 
            ha='center', va='top', fontsize=18, weight='bold', color='#2C3E50')
    
    # 根节点
    root_x, root_y = 8, 7.5
    draw_matrix(ax, root_x, root_y, current_state, size=1.2, 
               label='Root (Current)', label_color='#E74C3C', fontsize=13)
    
    # 第一层
    level1_y = 5.0
    level1_nodes = root.children
    spacing1 = 5.0
    start_x1 = root_x - (len(level1_nodes) - 1) * spacing1 / 2
    
    level1_positions = []
    for i, child in enumerate(level1_nodes):
        x = start_x1 + i * spacing1
        y = level1_y
        level1_positions.append((x, y, child))
        
        is_goal = (child.state == goal_state)
        label = f"Depth 1"
        if is_goal:
            label = "Goal State!"
        
        color = '#3498DB' if not is_goal else '#27AE60'
        ax.plot([root_x, x], [root_y - 0.6, y + 0.6], color=color, linewidth=3, zorder=1)
        ax.annotate('', xy=(x, y + 0.6), xytext=(root_x, root_y - 0.6),
                   arrowprops=dict(arrowstyle='->', color=color, lw=2))
        
        mid_x, mid_y = (root_x + x) / 2, (root_y + y) / 2
        bbox_props = dict(boxstyle="round,pad=0.25", facecolor='white', 
                         edgecolor=color, linewidth=1.5)
        ax.text(mid_x, mid_y, child.move_dir, ha='center', va='center',
               fontsize=10, weight='bold', color=color, bbox=bbox_props)
        
        draw_matrix(ax, x, y, child.state, size=1.0, highlight=is_goal,
                   label=label, label_color='#27AE60' if is_goal else '#34495E', fontsize=11)
    
    # 第二层
    level2_y = 2.5
    for px, py, parent in level1_positions:
        children = parent.children
        if len(children) == 0:
            continue
        
        spacing2 = 1.2 if len(children) <= 3 else 1.0
        start_x2 = px - (len(children) - 1) * spacing2 / 2
        
        for j, child in enumerate(children):
            x = start_x2 + j * spacing2
            y = level2_y
            is_goal = (child.state == goal_state)
            
            ax.plot([px, x], [py - 0.5, y + 0.5], color='#95A5A6', linewidth=1.5, zorder=1)
            
            mid_x, mid_y = (px + x) / 2, (py + y) / 2
            ax.text(mid_x, mid_y, child.move_dir, ha='center', va='center',
                   fontsize=8, color='#7F8C8D', style='italic',
                   bbox=dict(boxstyle='round,pad=0.2', facecolor='white', 
                            edgecolor='#BDC3C7', linewidth=0.5))
            
            label = f"Depth 2"
            if is_goal:
                label = "Goal!"
            draw_matrix(ax, x, y, child.state, size=0.9, highlight=is_goal,
                       label=label, label_color='#27AE60' if is_goal else '#7F8C8D', fontsize=10)
    
    # 底部统计
    stats_y = 0.8
    stats_text = (f'Tree Statistics: Total Nodes = 9  |  Branching Factor ≈ 3  |  '
                  f'Pruning: Avoid parent state  |  Search Space: 181,440 states')
    ax.text(8, stats_y, stats_text, ha='center', va='center', fontsize=11, color='#34495E',
           bbox=dict(boxstyle='round,pad=0.6', facecolor='white', 
                    edgecolor='#BDC3C7', linewidth=1.5))
    
    plt.tight_layout()
    
    # 保存（可以改格式为svg/pdf/png）
    plt.savefig('/workspaces/Algorithm_Alchemist/Research_Algorthm/方案1：局部搜索树（Local search tree）.png', dpi=600, bbox_inches='tight', pad_inches=0.3)
    print("图像已保存为 search_space_tree.png")
    
    plt.show()
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from collections import deque
import os

# ========== 配置 ==========
plt.rcParams['font.family'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 保存路径（可修改为你自己的路径）
SAVE_DIR = "/workspace/algorithm_alchemist/Research_Algorthm/"
os.makedirs(SAVE_DIR, exist_ok=True)

# ========== 辅助函数 ==========
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

def draw_matrix(ax, center_x, center_y, state, size=0.8, highlight=False, 
                label=None, label_color='black', fontsize=12):
    """绘制3x3状态矩阵"""
    cell_size = size / 3
    start_x = center_x - size / 2
    start_y = center_y - size / 2
    
    matrix = [state[i:i+3] for i in range(0, 9, 3)]
    
    # 绘制背景
    if highlight:
        rect = FancyBboxPatch((start_x - 0.05, start_y - 0.05), size + 0.1, size + 0.1,
                              boxstyle="round,pad=0.02", facecolor='#E8F8F5', 
                              edgecolor='#27AE60', linewidth=3)
        ax.add_patch(rect)
    else:
        # 阴影效果
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
            y = start_y + (2-row) * cell_size  # 注意行顺序反转
            
            # 交替背景色
            if (row + col) % 2 == 0:
                ax.add_patch(plt.Rectangle((x, y), cell_size, cell_size, 
                                          facecolor='#F8F9FA', edgecolor='#BDC3C7', linewidth=1))
            else:
                ax.add_patch(plt.Rectangle((x, y), cell_size, cell_size, 
                                          facecolor='white', edgecolor='#BDC3C7', linewidth=1))
            
            # 绘制数字
            num = matrix[row][col]
            text = str(num)
            color = '#E74C3C' if num == -1 else '#2C3E50'  # -1用红色
            weight = 'bold' if num == -1 else 'normal'
            ax.text(x + cell_size/2, y + cell_size/2, text, 
                   ha='center', va='center', fontsize=fontsize, 
                   color=color, weight=weight)
    
    # 绘制标签
    if label:
        ax.text(center_x, start_y - 0.15, label, ha='center', va='top', 
               fontsize=11, color=label_color, weight='bold')

# ========== 主程序 ==========
if __name__ == "__main__":
    # 当前状态和目标状态
    current_state = [0, 1, 2, 3, 4, 5, 6, -1, 7]
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, -1]
    neighbors = get_neighbors(current_state)
    
    # 创建画布
    fig, ax = plt.subplots(figsize=(12, 8), dpi=600)  # 600dpi高清
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_facecolor('#FAFBFC')
    
    # 标题
    ax.text(6, 7.5, 'Search Space: State Transition Graph', 
            ha='center', va='top', fontsize=18, weight='bold', color='#2C3E50')
    
    # 中心状态（当前）
    center_x, center_y = 6, 4
    draw_matrix(ax, center_x, center_y, current_state, size=1.2, 
                label='Current State', label_color='#2980B9', fontsize=14)
    
    # 邻居位置配置（上、左、右）
    positions = [
        (6, 6.5, "Up", "#E74C3C"),
        (2.5, 4, "Left", "#F39C12"),
        (9.5, 4, "Right", "#27AE60"),
    ]
    
    for i, (nx, ny, direction, color) in enumerate(positions):
        if i < len(neighbors):
            state, move_name = neighbors[i]
            is_goal = (state == goal_state)
            
            # 绘制箭头
            if direction == "Up":
                ax.annotate('', xy=(nx, ny - 0.6), xytext=(center_x, center_y + 0.6),
                           arrowprops=dict(arrowstyle='->', color=color, lw=3))
                mid_x, mid_y = (center_x + nx) / 2, (center_y + ny) / 2
            elif direction == "Left":
                ax.annotate('', xy=(nx + 0.6, ny), xytext=(center_x - 0.6, center_y),
                           arrowprops=dict(arrowstyle='->', color=color, lw=3))
                mid_x, mid_y = (center_x + nx) / 2, center_y
            else:  # Right
                ax.annotate('', xy=(nx - 0.6, ny), xytext=(center_x + 0.6, center_y),
                           arrowprops=dict(arrowstyle='->', color=color, lw=3))
                mid_x, mid_y = (center_x + nx) / 2, center_y
            
            # 移动方向标签
            bbox_props = dict(boxstyle="round,pad=0.3", facecolor='white', edgecolor=color, linewidth=2)
            ax.text(mid_x, mid_y, move_name, ha='center', va='center', 
                   fontsize=11, weight='bold', color=color, bbox=bbox_props)
            
            # 绘制邻居状态
            label_text = f"Move: {move_name}"
            if is_goal:
                label_text = "Goal State!"
            draw_matrix(ax, nx, ny, state, size=1.0, highlight=is_goal,
                       label=label_text, label_color='#27AE60' if is_goal else color, fontsize=12)
    
    # 底部图例
    legend_y = 1.2
    ax.text(6, legend_y, 'Legend: Red=Regular Move | Orange=Regular Move | Green=Optimal Move (Reaches Goal)', 
           ha='center', fontsize=10, color='#34495E',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#BDC3C7'))
    
    plt.tight_layout()
    
    # 保存高清图
    save_path = os.path.join(SAVE_DIR, "方案2：状态转移图（State Transition Graph）.png")
    plt.savefig(save_path, format='png', dpi=600, bbox_inches='tight', pad_inches=0.3)
    print(f"✅ 图像已保存至: {save_path}")
    print(f"📊 图像规格: 600dpi，尺寸 {fig.get_size_inches()[0]}x{fig.get_size_inches()[1]} 英寸")
    
    plt.show()
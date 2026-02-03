import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from collections import deque
import os

# ========== Font Settings ==========
plt.rcParams['font.family'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# ========== Labels (All English) ==========
LABELS = {
    'title': 'Search Path: Shortest Solution (BFS Algorithm)',
    'initial': 'Initial State',
    'goal': 'Goal State',
    'step': 'Step',
    'cost': 'g',
    'stats': 'Path Length: {steps} moves | Algorithm: BFS (Breadth-First Search) | Guarantees shortest path'
}

# ========== Helper Functions ==========
def find_blank(state):
    """Find position of blank tile (-1)"""
    return state.index(-1)

def get_neighbors(state):
    """Get all possible neighbor states"""
    neighbors = []
    blank_idx = find_blank(state)
    row, col = blank_idx // 3, blank_idx % 3
    
    directions = [
        (-1, 0, "Up"), 
        (1, 0, "Down"), 
        (0, -1, "Left"), 
        (0, 1, "Right")
    ]
    
    for dr, dc, name in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = state.copy()
            new_state[blank_idx], new_state[new_idx] = new_state[new_idx], new_state[blank_idx]
            neighbors.append((new_state, name))
    return neighbors

def bfs_path(start, goal):
    """Find shortest path using BFS"""
    if start == goal:
        return [start]
    queue = deque([(start, [start])])
    visited = {tuple(start)}
    
    while queue:
        current, path = queue.popleft()
        for next_state, _ in get_neighbors(current):
            next_tuple = tuple(next_state)
            if next_tuple not in visited:
                if next_state == goal:
                    return path + [next_state]
                visited.add(next_tuple)
                queue.append((next_state, path + [next_state]))
    return None

def draw_matrix(ax, center_x, center_y, state, size=0.8, highlight=False, 
                label=None, label_color='black', fontsize=12):
    """Draw a 3x3 state matrix"""
    cell_size = size / 3
    start_x = center_x - size / 2
    start_y = center_y - size / 2
    
    matrix = [state[i:i+3] for i in range(0, 9, 3)]
    
    if highlight:
        rect = FancyBboxPatch(
            (start_x - 0.05, start_y - 0.05), size + 0.1, size + 0.1,
            boxstyle="round,pad=0.02", facecolor='#E8F8F5', 
            edgecolor='#27AE60', linewidth=3
        )
        ax.add_patch(rect)
    else:
        # Shadow effect
        shadow = FancyBboxPatch(
            (start_x + 0.02, start_y - 0.02), size, size,
            boxstyle="round,pad=0.01", facecolor='gray', alpha=0.2
        )
        ax.add_patch(shadow)
        rect = FancyBboxPatch(
            (start_x, start_y), size, size,
            boxstyle="round,pad=0.01", facecolor='white', 
            edgecolor='#2C3E50', linewidth=2
        )
        ax.add_patch(rect)
    
    # Draw cells
    for row in range(3):
        for col in range(3):
            x = start_x + col * cell_size
            y = start_y + (2-row) * cell_size
            
            if (row + col) % 2 == 0:
                ax.add_patch(plt.Rectangle(
                    (x, y), cell_size, cell_size, 
                    facecolor='#F8F9FA', edgecolor='#BDC3C7', linewidth=1
                ))
            else:
                ax.add_patch(plt.Rectangle(
                    (x, y), cell_size, cell_size, 
                    facecolor='white', edgecolor='#BDC3C7', linewidth=1
                ))
            
            # Draw number
            num = matrix[row][col]
            text = str(num)
            color = '#E74C3C' if num == -1 else '#2C3E50'
            weight = 'bold' if num == -1 else 'normal'
            ax.text(
                x + cell_size/2, y + cell_size/2, text, 
                ha='center', va='center', fontsize=fontsize, 
                color=color, weight=weight
            )
    
    # Draw label
    if label:
        ax.text(
            center_x, start_y - 0.15, label, 
            ha='center', va='top', fontsize=11, 
            color=label_color, weight='bold'
        )

# ========== Main Program ==========
if __name__ == "__main__":
    # Set save path
    save_dir = "/workspace/algorithm_alchemist/Research_Algorthm/"
    os.makedirs(save_dir, exist_ok=True)
    
    # Start and goal states
    start_state = [0, 1, 2, 3, -1, 5, 6, 4, 7]
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, -1]
    
    # Search for path
    path = bfs_path(start_state, goal_state)
    
    # Create figure
    fig, ax = plt.subplots(figsize=(14, 6), dpi=600)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis('off')
    ax.set_facecolor('#F5F7FA')
    
    # Title
    ax.text(
        7, 5.7, LABELS['title'], 
        ha='center', va='top', fontsize=18, weight='bold', color='#2C3E50'
    )
    
    # Draw path
    start_x = 2.5
    center_y = 3.0
    spacing = 4.5
    
    for i, state in enumerate(path):
        x = start_x + i * spacing
        is_goal = (state == goal_state)
        is_start = (i == 0)
        
        if is_start:
            label = LABELS['initial']
            color = '#E74C3C'
        elif is_goal:
            label = LABELS['goal']
            color = '#27AE60'
        else:
            label = f"{LABELS['step']} {i}"
            color = '#3498DB'
        
        draw_matrix(
            ax, x, center_y, state, size=1.3, highlight=is_goal,
            label=label, label_color=color, fontsize=13
        )
        
        if i < len(path) - 1:
            next_x = start_x + (i + 1) * spacing
            ax.annotate(
                '', xy=(next_x - 0.75, center_y), xytext=(x + 0.75, center_y),
                arrowprops=dict(arrowstyle='->', color='#34495E', lw=4)
            )
            
            # Determine move direction
            blank_now = state.index(-1)
            blank_next = path[i+1].index(-1)
            if blank_next == blank_now - 3:
                move = "↑ Up"
            elif blank_next == blank_now + 3:
                move = "↓ Down"
            elif blank_next == blank_now - 1:
                move = "← Left"
            else:
                move = "→ Right"
            
            mid_x = (x + next_x) / 2
            bbox_props = dict(
                boxstyle="round,pad=0.3", facecolor='#F39C12', 
                edgecolor='#E67E22', linewidth=2
            )
            ax.text(
                mid_x, center_y + 0.8, move, 
                ha='center', va='center', fontsize=11, 
                weight='bold', color='white', bbox=bbox_props
            )
            
            # Cost label
            cost_text = f"{LABELS['cost']}={i+1}"
            ax.text(
                mid_x, center_y - 0.8, cost_text, 
                ha='center', va='center', fontsize=10, 
                color='#7F8C8D', style='italic'
            )
    
    # Statistics
    stats_text = LABELS['stats'].format(steps=len(path)-1)
    ax.text(
        7, 0.8, stats_text, 
        ha='center', va='center', fontsize=11, color='#34495E',
        bbox=dict(
            boxstyle='round,pad=0.6', facecolor='white', 
            edgecolor='#BDC3C7', linewidth=1.5
        )
    )
    
    plt.tight_layout()
    
    # Save
    save_path = os.path.join(save_dir, "方案3：搜索路径图（Solution Path）.png")
    plt.savefig(save_path, format='png', dpi=600, bbox_inches='tight', pad_inches=0.3)
    print(f"Saved to: {save_path}")
    plt.show()
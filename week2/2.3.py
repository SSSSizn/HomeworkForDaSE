from collections import deque

def can_cross(state):
    # 检查是否在任何一边都没有人的情况下，狼会吃羊，羊会吃白菜
    if (state['wolf'] == 1 and state['sheep'] == 1 and state['cabbage'] == 0) or \
       (state['wolf'] == 0 and state['sheep'] == 1 and state['cabbage'] == 1):
        return False
    return True

def is_goal(state):
    # 所有物品都移到对岸，即目标状态
    return state == {'wolf': 0, 'sheep': 0, 'cabbage': 0, 'boat': 0}

def bfs(initial_state):
    queue = deque()
    queue.append((initial_state, []))  # 存储状态和路径

    while queue:
        current_state, path = queue.popleft()

        if is_goal(current_state):
            # 如果达到目标状态，返回路径
            return path

        for item in ['wolf', 'sheep', 'cabbage']:
            if current_state[item] == current_state['boat']:
                new_state = current_state.copy()
                new_state[item] = 1 - current_state[item]
                new_state['boat'] = 1 - current_state['boat']

                if can_cross(new_state):
                    new_path = path + [f"Take {item}"]
                    queue.append((new_state, new_path))

# 初始状态，人、狼、羊、白菜都在一边（1表示一边，0表示另一边）
initial_state = {'wolf': 1, 'sheep': 1, 'cabbage': 1, 'boat': 1}

result = bfs(initial_state)
print("人过河的方案有：")
print(result)


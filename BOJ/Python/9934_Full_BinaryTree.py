K = int(input())

building_order = list(map(int, input().split()))

tree = [0 for _ in range(2 ** K)]
cur_idx = 0
    
def inorder_traversal(node):
    global cur_idx
    if node <= 2**K - 1:
        inorder_traversal(node * 2) # 왼쪽 노드
        tree[node] = building_order[cur_idx]
        cur_idx+=1
        inorder_traversal(node * 2 + 1) # 오른쪽 노드
    
    # print(building_order[cur_idx])
        
inorder_traversal(1)

end = 1
start = 1


while end < 2**K:
    print(*tree[start:end+1])
    
    start = end+1
    end = end*2+1
    
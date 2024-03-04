N = int(input())

arr = [(idx, int(num)) for idx, num in enumerate(input().split())]

arr.sort(key=lambda x:x[1])

# print(arr)

tree = [0 for _ in range(4*N)] # Segtree Init

def merge(a, b): # Range Sum Functions
    return a+b


def query(left, right):
    return query_rec(1, left, right, 0, N-1) # All Range

def query_rec(node, left, right, node_left, node_right):
    
    if node_right < left or right < node_left: # Out of Range
        return 0 # No Effect
    
    if left <= node_left and node_right <= right: # Full Range
        return tree[node]
    
    node_mid = (node_left + node_right) // 2
    
    return merge(query_rec(node*2, left, right, node_left, node_mid),
                 query_rec(node*2+1, left, right, node_mid+1, node_right))
    
def update(idx, new_value): # 어떤 idx의 노드를 어떤 값으로 바꿀 것 인가
    update_rec(1, idx, new_value, 0, N-1)

def update_rec(node, idx, new_value, left_node, right_node):
    
    if idx < left_node or right_node < idx: # Out of Range
        return tree[node] # No Effect
    
    if left_node == right_node:
        tree[node] = new_value
        return tree[node]
    
    mid_node = (left_node + right_node) // 2
    
    tree[node] = merge(update_rec(node*2, idx, new_value, left_node, mid_node),
                       update_rec(node*2+1, idx, new_value, mid_node+1, right_node))
    
    return tree[node]

def print_tree():
    for i in range(int( 2*N ** 0.5)):
        print(tree[2 ** i: (2**i) *2])
    
if __name__ == "__main__":
    
    cnt = 0
    
    for idx, num in arr:
        # print(idx, num)
        cnt += query(idx+1, N-1) # 자기보다 오른쪽에 있는 수중에 작은 수의 갯수
        update(idx, 1)
        
        # print_tree()
        
    print(cnt)
        
    
    
    



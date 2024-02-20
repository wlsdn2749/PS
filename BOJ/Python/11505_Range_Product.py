def merge(a, b):
    return (a * b) % 1_000_000_007

def build(arr):
    build_rec(arr, 1, 0, N-1)
    
def build_rec(arr, node, left, right):
    if left == right:
        tree[node] = arr[left]
        return tree[node]
    
    mid = (left + right) // 2
    tree[node] = merge(build_rec(arr, node*2, left, mid),
                       build_rec(arr, node*2+1, mid+1, right))
    
    return tree[node]

def query(left, right):
    return query_rec(left, right, 1, 0, N-1)

def query_rec(left, right, node, left_node, right_node):
    
    # out of range 
    if right < left_node or right_node < left:
        return 1
    
    if left <= left_node and right_node <= right:
        return tree[node]
    
    mid_node = (left_node + right_node) // 2
    
    return merge(query_rec(left, right, node*2, left_node, mid_node),
                 query_rec(left, right, node*2+1, mid_node+1, right_node))
    

def update(index, new_value):
    update_rec(index, new_value, 1, 0, N-1)

def update_rec(index, new_value, node, left_node, right_node):
    # out of range
    if index < left_node or right_node < index:
        return tree[node]
    
    # change
    if left_node == right_node:
        tree[node] = new_value
        return tree[node]
        
    mid = (left_node + right_node)//2
    tree[node] = merge(update_rec(index, new_value, node*2, left_node, mid),
                       update_rec(index, new_value, node*2+1, mid+1, right_node)
                       )
    return tree[node]
        
    
    
    
    


if __name__ == "__main__":
    N, M, K = map(int, input().split())
    
    arr = []
    tree = [0 for _ in range(4*N)] # initial tree
    
    for i in range(N):
        arr.append(int(input()))
        
    build(arr)
    
    for i in range(M+K):
        a,b,c = map(int, input().split())
        
        if a == 1:
            update(b-1,c)
        elif a == 2:
            print(query(b-1,c-1))
            # print(tree)
    
    
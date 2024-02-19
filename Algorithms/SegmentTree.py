def merge(left: int, right: int) -> int:
    # 합 연산
    return left + right

def build(arr: list) -> None:
    build_rec(arr, 1, 0, N-1)
    

def build_rec(arr, node, node_left, node_right) -> int:
    # 만약 리프노드일 경우
    if node_left == node_right: 
        tree[node] = arr[node_left]
        return tree[node]
    
    # 중간 지점
    mid = (node_left + node_right) // 2 
    
    left_value = build_rec(arr, node*2, node_left, mid)
    right_value = build_rec(arr, node*2+1 , mid+1, node_right)
    
    tree[node] = merge(left_value, right_value)
    return tree[node]

def query(left, right) -> int:
    return query_rec(left, right, 1, 0, N-1)

def query_rec(left, right, node, node_left, node_right) -> int:
    # node를 포함하는 범위가 left와 right를 벗어날 경우 default 값 = 0 리턴
    if node_right < left or right < node_left:
        return 0
    
    # node를 포함하는 범위가 left와 right를 완전히 포함하는 경우 tree[node] 리턴
    if left <= node_left and node_right <= right:
        return tree[node]
    
    
    # 걸쳐 있는 경우
    mid = (node_left + node_right) // 2
    return merge(query_rec(left, right, node*2, node_left, mid),
                 query_rec(left, right, node*2+1, mid+1, node_right))

def update(index, value) -> None:
    update_rec(index, value, 1, 0, N-1)

def update_rec(index, value, node, node_left, node_right):
    #범위를 벗어나면 그냥 그대로 리턴
    if index < node_left or node_right < index:
        return tree[node]
    
    # 범위를 벗어나지 않았다는 전제하여 같으면 index는 핫아 node_left == node_right 임
    if node_left == node_right:
        tree[node] = value
        return tree[node]
    
    mid = (node_left + node_right) // 2
    tree[node] = merge(update_rec(index, value, node*2, node_left, mid),
                       update_rec(index, value, node*2+1, mid+1, node_right))
    
    return tree[node]
    
    
    
def print_tree():
    for i in range(int( 2*N ** 0.5)):
        print(tree[2 ** i: (2**i) *2])
        
if __name__ == "__main__":
    N = 10
    arr = [10, 24, 59, 4, 29, 40, 30, 90, 11, 33]
    
    tree = [0 for _ in range(N*4)] ## init
    build(arr) # build

    print_tree()
    
    update(index=5, value=100)
    
    print_tree()
    # print(query(0, 1)) # 34
    # print(query(8, 9)) # 44
    
    
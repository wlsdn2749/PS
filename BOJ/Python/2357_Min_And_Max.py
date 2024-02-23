import sys

N, M = map(int, input().split())

arr = []

tree = [0 for _ in range(4*N)]

for i in range(N):
    arr.append(int(input()))
    
def merge(t_a: tuple, t_b: tuple) -> tuple:
    # tuple(min, max) return
    return (min(t_a[0], t_b[0]),
            max(t_a[1], t_b[1]))
    
    
def build(arr):
    build_rec(arr, 1, 0, N-1)
    
def build_rec(arr, node, left, right):
    if left == right:
        tree[node] = (arr[left], arr[left]) # (min, max)
        return tree[node]
    
    mid = (left + right) // 2
    tree[node] = merge(build_rec(arr, node*2, left, mid),
                       build_rec(arr, node*2+1, mid+1, right))
    
    return tree[node]

def query(left, right):
    return query_rec(left, right, 1, 0, N-1)
    
def query_rec(left, right, node, node_left, node_right):
    # Out of Range
    if right < node_left or node_right < left:
        return (1_000_000_000, 0) # min, max에 영향을 주지 않는 값
    
    # Fully Included
    if left <= node_left and node_right <= right:
        return tree[node]
    
    node_mid = (node_left + node_right) // 2
    
    return merge(query_rec(left, right, node*2, node_left, node_mid),
                 query_rec(left, right, node*2+1, node_mid+1, node_right)) 
    
build(arr)

for i in range(M):
    a, b = map(int, input().split())
    print(*query(a-1, b-1))
    
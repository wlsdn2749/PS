N = int(input())

tree = [[] for _ in range(N+1)]


def dfs(node: int):
    leaf = 0

    if not tree[node]: # leaf        
        return 1
    
    for i in tree[node]:
        leaf += dfs(i)

    return leaf

root = 0
    
for idx, node in enumerate(list(map(int, input().split()))):
    if node == -1:
        root = idx
        
    tree[node].append(idx)
        
eliminate = int(input())

for idx, node in enumerate(tree):
    if eliminate in node:
        tree[idx].remove(eliminate)

leaf = dfs(root)

if eliminate == root:
    leaf = 0    
print(leaf)
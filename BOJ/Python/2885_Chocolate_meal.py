from typing import Tuple

def _input():
    K = int(input())
    
    return K

def get_two_multiplier_bt_K(K):
    li = []
    indice = 1
    
    while True:
        
        if indice >= K:
            li.append(indice)
            break
        
        li.append(indice)
        indice *= 2
        
    return li[-1]
    
def solution(K: int) -> Tuple[int, int]:
    
    mul = get_two_multiplier_bt_K(K)
    r_mul = mul
    cnt = 0
    
    if mul == K:
        return r_mul, cnt
    
    while True:
        mul = t = mul // 2
        cnt += 1
        
        if K >= t:            
            K = K - t    
        
        if K == 0:
            break
                
    return r_mul, cnt
    
if __name__ == "__main__":
    K = _input()
    
    S, cnt = solution(K)
    
    print(S, cnt)
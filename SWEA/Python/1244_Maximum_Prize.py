import sys
# from itertools import combinations
# sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def list_to_integer(lst):
    result = int(''.join(lst))
    return result

def bt(k):
    
    max_values = list_to_integer(number)
    if max_values in result[k]:    
        return max_values
    else:
        result[k].append(max_values)
        
    if k == 0:
        return max_values
        
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            if i == j:
                continue
            else:
                number[i], number[j] = number[j], number[i]
                max_values = max(max_values, bt(k-1))
                number[i], number[j] = number[j], number[i]
    
    return max_values
    
for test_case in range(1, T + 1):
    number, k = input().split()
    number = list(map(str, number))
    k = int(k)
    
    result = [[] for _ in range(k+1)]
    max_values = bt(k)
    print(f"#{test_case} {max(result[0])}")    
    
    